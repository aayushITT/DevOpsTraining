import json
import logging
from utils.sns_helper import publish_to_sns        # For sending SNS notifications
from utils.sqs_helper import SQSClient             # Custom class for handling SQS logic

# Configure logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define SNS topic ARN and SQS queue URL (make sure these match your AWS setup)
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:536697246803:file-upload-notification"
SQS_QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/536697246803/file-process-queue"

def lambda_handler(event, context):
    """
    Triggered when a file is uploaded to S3 (specifically a .zip).
    Sends notification via SNS and queues the file info in SQS for processing.
    """
    logger.info("S3 Event Received")  # Log entry point

    # Loop through each record (file upload event)
    for record in event['Records']:
        # Extract bucket name and object key (file name)
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # Construct S3 path string
        s3_path = f"s3://{bucket}/{key}"

        # Compose and send SNS notification
        message = f"New ZIP uploaded: {s3_path}"
        publish_to_sns(SNS_TOPIC_ARN, message)

        # Create SQS client and send message with file details
        sqs = SQSClient(SQS_QUEUE_URL)
        sqs.send_message(json.dumps({"bucket": bucket, "key": key}))

    # Return success response to AWS Lambda
    return {"statusCode": 200, "body": "Processed S3 event"}
