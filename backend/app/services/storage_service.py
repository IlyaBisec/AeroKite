# Storage service
# ilya_bisec
# Date: 25/08/2026 15:08

import uuid

import boto3
from rsa import key

from app.core.config import settings

s3 = boto3.resource("s3",
                    endpoint_url=settings.AWS_S3_ENDPOINT,
                    aws_access_key_id=settings.S3_ACCESS_KEY,
                    aws_secret_access_key=settings.S3_SECRET_KEY)

BUCKET = settings.S3_BUCKET

def upload_file(file_obj, key):
    """Upload a file to S3"""
    s3.upload_fileobj(file_obj, BUCKET, key)


def generate_url():
    """Generate a unique ID"""
    return s3.generate_presigned_url("get_object", Params={"Bucket": BUCKET, "Key": key}, ExpiresIn=3600)

