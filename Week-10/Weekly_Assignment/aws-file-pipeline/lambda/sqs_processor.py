import os
import json
import uuid
import pandas as pd
import logging
from utils.sqs_helper import SQSClient
from utils.s3_helper import download_file, upload_file, extract_zip
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
SQS_QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/536697246803/file-process-queue"
OUTPUT_BUCKET = "devops-python-assignment"
TEMP_DIR = "/tmp"
 
class FileProcessor(SQSClient):
    def __init__(self, queue_url):
        super().__init__(queue_url)
 
    def process(self):
        messages = self.fetch_messages()
        for msg in messages:
            body = json.loads(msg['Body'])
            bucket, key = body['bucket'], body['key']
 
            zip_file_path = os.path.join(TEMP_DIR, str(uuid.uuid4()) + ".zip")
            extract_path = os.path.join(TEMP_DIR, str(uuid.uuid4()))
            os.makedirs(extract_path, exist_ok=True)
 
            download_file(bucket, key, zip_file_path)
            extract_zip(zip_file_path, extract_path)
 
            for fname in os.listdir(extract_path):
                fpath = os.path.join(extract_path, fname)
                if fname.endswith(".txt") or fname.endswith(".json"):
                    df = self.convert_to_csv(fpath)
                    csv_key = "output/" + fname.rsplit(".", 1)[0] + ".csv"
                    csv_path = os.path.join(TEMP_DIR, fname.rsplit(".", 1)[0] + ".csv")
                    df.to_csv(csv_path, index=False)
                    upload_file(OUTPUT_BUCKET, csv_key, csv_path)
 
            self.delete_message(msg['ReceiptHandle'])
 
    def convert_to_csv(self, filepath):
        if filepath.endswith(".txt"):
            with open(filepath, "r") as f:
                data = [line.strip().split(",") for line in f.readlines()]
                return pd.DataFrame(data[1:], columns=data[0])
        elif filepath.endswith(".json"):
            return pd.read_json(filepath)
        return pd.DataFrame()
 
def lambda_handler(event, context):
    processor = FileProcessor(SQS_QUEUE_URL)
    processor.process()