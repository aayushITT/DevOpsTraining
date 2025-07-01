import os
import json
import uuid
import pandas as pd
import logging

# Import custom utilities
from utils.sqs_helper import SQSClient                    # Base class for SQS operations
from utils.s3_helper import download_file, upload_file, extract_zip  # S3-related helpers

# Logger configuration
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS resource constants
SQS_QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/536697246803/file-process-queue"
OUTPUT_BUCKET = "devops-python-assignment"
TEMP_DIR = "/tmp"  # Lambda's temporary filesystem

# Custom class that extends SQSClient for file processing
class FileProcessor(SQSClient):
    def __init__(self, queue_url):
        super().__init__(queue_url)  # Inherit SQS methods

    def process(self):
        # Fetch messages from SQS queue
        messages = self.fetch_messages()

        # Iterate through all messages
        for msg in messages:
            body = json.loads(msg['Body'])         # Parse JSON message body
            bucket, key = body['bucket'], body['key']  # Extract S3 info

            # Generate unique file paths to avoid collisions
            zip_file_path = os.path.join(TEMP_DIR, str(uuid.uuid4()) + ".zip")
            extract_path = os.path.join(TEMP_DIR, str(uuid.uuid4()))
            os.makedirs(extract_path, exist_ok=True)

            # Download and extract zip file
            download_file(bucket, key, zip_file_path)
            extract_zip(zip_file_path, extract_path)

            # Iterate over each extracted file
            for fname in os.listdir(extract_path):
                fpath = os.path.join(extract_path, fname)
                
                # Process only .txt and .json files
                if fname.endswith(".txt") or fname.endswith(".json"):
                    df = self.convert_to_csv(fpath)  # Convert file to pandas DataFrame

                    # Prepare output paths
                    csv_key = "output/" + fname.rsplit(".", 1)[0] + ".csv"
                    csv_path = os.path.join(TEMP_DIR, fname.rsplit(".", 1)[0] + ".csv")
                    
                    # Save to CSV and upload to output bucket
                    df.to_csv(csv_path, index=False)
                    upload_file(OUTPUT_BUCKET, csv_key, csv_path)

            # After processing, delete the message from SQS
            self.delete_message(msg['ReceiptHandle'])

    def convert_to_csv(self, filepath):
        # Convert a .txt or .json file to pandas DataFrame
        if filepath.endswith(".txt"):
            with open(filepath, "r") as f:
                data = [line.strip().split(",") for line in f.readlines()]
                return pd.DataFrame(data[1:], columns=data[0])  # Assumes first line is header
        elif filepath.endswith(".json"):
            return pd.read_json(filepath)
        return pd.DataFrame()  # Return empty DataFrame for unsupported files

# Lambda entry point
def lambda_handler(event, context):
    processor = FileProcessor(SQS_QUEUE_URL)
    processor.process()
