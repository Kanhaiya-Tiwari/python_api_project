import boto3

def get_bucket_list():
    """
    Get list of S3 buckets from AWS
    """
    try:
        s3_client = boto3.client('s3')
        response = s3_client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return {"buckets": buckets, "status": "success"}
    except Exception as e:
        raise Exception(f"Failed to fetch buckets: {str(e)}")