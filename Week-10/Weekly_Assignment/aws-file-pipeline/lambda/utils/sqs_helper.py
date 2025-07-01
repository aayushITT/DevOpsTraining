import boto3
import logging

# Set up basic logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class SQSClient:
    """
    A reusable class to interact with AWS SQS.
    Handles sending, receiving, and deleting messages.
    """

    def __init__(self, queue_url):
        """
        Initialize the SQS client with a specific queue URL.
        Args:
            queue_url (str): The URL of the SQS queue.
        """
        self.queue_url = queue_url
        self.client = boto3.client('sqs')

    def send_message(self, message_body):
        """
        Send a message to the configured SQS queue.

        Args:
            message_body (str): The content of the message to be sent.

        Returns:
            dict: Response from SQS send_message API.
        """
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
        """
        Fetch messages from the queue.

        Args:
            max_messages (int): Number of messages to fetch (default is 1).

        Returns:
            list: A list of message dictionaries, or an empty list if none.
        """
        try:
            response = self.client.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=max_messages,
                WaitTimeSeconds=10  # Long polling for better efficiency
            )
            return response.get('Messages', [])
        except Exception as e:
            logger.error(f"Error fetching messages: {e}")
            return []

    def delete_message(self, receipt_handle):
        """
        Delete a message from the queue after processing.

        Args:
            receipt_handle (str): The unique receipt handle of the message.
        """
        try:
            self.client.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=receipt_handle
            )
            logger.info("Deleted message from SQS")
        except Exception as e:
            logger.error(f"Error deleting message: {e}")
