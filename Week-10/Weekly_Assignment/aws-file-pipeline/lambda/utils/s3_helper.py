import boto3
import os
import zipfile
import logging

# Initialize logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize S3 client using boto3
s3 = boto3.client('s3')


def download_file(bucket, key, download_path):
    """
    Download a file from the specified S3 bucket and key to a local path.
    Args:
        bucket (str): S3 bucket name
        key (str): S3 object key (path inside the bucket)
        download_path (str): Local path to save the downloaded file
    """
    try:
        s3.download_file(bucket, key, download_path)
        logger.info(f"Downloaded {key} from {bucket}")
    except Exception as e:
        logger.error(f"Download failed: {e}")
        raise


def upload_file(bucket, key, file_path):
    """
    Upload a local file to a specified S3 bucket and key.
    Args:
        bucket (str): S3 bucket name
        key (str): S3 object key (path to upload to)
        file_path (str): Local path of the file to upload
    """
    try:
        s3.upload_file(file_path, bucket, key)
        logger.info(f"Uploaded {key} to {bucket}")
    except Exception as e:
        logger.error(f"Upload failed: {e}")
        raise


def extract_zip(zip_path, extract_to):
    """
    Extract the contents of a .zip file to a target directory.
    Args:
        zip_path (str): Path to the zip file to extract
        extract_to (str): Directory where contents will be extracted
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        logger.info(f"Extracted {zip_path}")
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise
