import json
import logging
from utils.sns_helper import publish_to_sns
from utils.sqs_helper import SQSClient
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:536697246803:file-upload-notification"
SQS_QUEUE_URL = "https://sqs.ap-south-1.amazonaws.com/536697246803/file-process-queue"
 
def lambda_handler(event, context):
    logger.info("S3 Event Received")
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        s3_path = f"s3://{bucket}/{key}"
 
        message = f"New ZIP uploaded: {s3_path}"
        publish_to_sns(SNS_TOPIC_ARN, message)
 
        sqs = SQSClient(SQS_QUEUE_URL)
        sqs.send_message(json.dumps({"bucket": bucket, "key": key}))
 
    return {"statusCode": 200, "body": "Processed S3 event"}