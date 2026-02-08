from fastapi import APIRouter, HTTPException
from services.aws_services import get_bucket_list
router = APIRouter()
@router.get("/s3",status_code=200)
def get_buckets():
    """
    Endpoint to get system metrics.
    """
    try:
        buckets_info = get_bucket_list()
        return buckets_info
    except:
        raise HTTPException(
            status_code=500, 
            detail="Internal Server Error"
            )