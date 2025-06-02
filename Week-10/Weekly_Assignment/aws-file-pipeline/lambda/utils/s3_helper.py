import boto3
import os
import zipfile
import logging
 
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
s3 = boto3.client('s3')
 
def download_file(bucket, key, download_path):
    try:
        s3.download_file(bucket, key, download_path)
        logger.info(f"Downloaded {key} from {bucket}")
    except Exception as e:
        logger.error(f"Download failed: {e}")
        raise
 
def upload_file(bucket, key, file_path):
    try:
        s3.upload_file(file_path, bucket, key)
        logger.info(f"Uploaded {key} to {bucket}")
    except Exception as e:
        logger.error(f"Upload failed: {e}")
        raise
 
def extract_zip(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        logger.info(f"Extracted {zip_path}")
    except Exception as e:
        logger.error(f"Extraction failed: {e}")
        raise