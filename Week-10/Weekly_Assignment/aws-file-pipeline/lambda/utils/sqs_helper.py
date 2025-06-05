import boto3
import logging
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
class SQSClient:
    def __init__(self, queue_url):
        self.queue_url = queue_url
        self.client = boto3.client('sqs')
 
    def send_message(self, message_body):
        try:
            response = self.client.send_message(
                QueueUrl=self.queue_url,
                MessageBody=message_body
            )
            logger.info("Message sent to SQS")
            return response
        except Exception as e:
            logger.error(f"Failed to send message to SQS: {e}")
            raise
 
    def fetch_messages(self, max_messages=1):
        try:
            response = self.client.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=max_messages,
                WaitTimeSeconds=10
            )
            return response.get('Messages', [])
        except Exception as e:
            logger.error(f"Error fetching messages: {e}")
            return []
 
    def delete_message(self, receipt_handle):
        try:
            self.client.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )
            logger.info("Deleted message from SQS")
        except Exception as e:
            logger.error(f"Error deleting message: {e}")

 