import boto3
from datetime import datetime

def get_bucket_list():
    """
    Get a list of all S3 buckets in the AWS account.
    """
    s3_client = boto3.client('s3')
    buckets = s3_client.list_buckets()["Buckets"]

    current_datetime = datetime.now()
    old_buckets = []
    new_buckets = []
    for bucket in buckets:
        bucket_name = bucket ["name"]
        new_buckets.append(bucket_name)

    return{
        "new buckets":new_buckets
    }