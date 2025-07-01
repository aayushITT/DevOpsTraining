import boto3
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def publish_to_sns(topic_arn, message, subject="S3 Upload Notification"):
    """
    Publishes a message to an SNS topic.

    Args:
        topic_arn (str): The ARN of the SNS topic to publish to.
        message (str): The message body/content to be sent.
        subject (str): The subject/title of the notification (optional).

    Returns:
        dict: Response from the SNS publish API.

    Raises:
        Exception: If the SNS publish call fails.
    """
    try:
        # Initialize SNS client
        sns = boto3.client('sns')

        # Publish the message to the SNS topic
        response = sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject
        )

        logger.info("SNS Notification Sent")
        return response
    except Exception as e:
        logger.error(f"Failed to publish to SNS: {e}")
        raise
