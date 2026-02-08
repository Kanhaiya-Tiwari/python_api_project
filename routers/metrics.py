from fastapi import APIRouter, HTTPException
from services.metrics_service import get_system_metrics
router = APIRouter()
@router.get("/metrics")
def read_metrics():
    """
    Endpoint to get system metrics.
    """
    try:
        metrics = get_system_metrics()
        return metrics
    except:
        raise HTTPException(
            status_code=500, 
            detail="Error retrieving system metrics"
            )