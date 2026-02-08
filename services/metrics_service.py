import psutil

def get_system_metrics():
    """
    Get system metrics such as CPU usage, memory usage, and disk usage.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory().percent
    disk_info = psutil.disk_usage('/').percent

    cpu_threshold = 10
    if cpu_usage > cpu_threshold:
        print(f"Warning: CPU usage is high at {cpu_usage}%") 
    else:
        print("healthy")

    return {
        "cpu_usage": cpu_usage,
        "memory_total": memory_info.total,
        "memory_used": memory_info.used,
        "memory_percent": memory_info.percent,
        "disk_total": disk_info.total,
        "disk_used": disk_info.used,
        "disk_percent": disk_info.percent
    }
