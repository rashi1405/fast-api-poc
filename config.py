import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# S3 Configuration
S3_BUCKET  = os.getenv("AWS_BUCKET_NAME")
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION     = os.getenv("AWS_REGION")

# Initialize boto3 client (shared everywhere)
s3_client = boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name=REGION
)
