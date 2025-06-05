import boto3
import logging
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
def publish_to_sns(topic_arn, message, subject="S3 Upload Notification"):
    try:
        sns = boto3.client('sns')
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