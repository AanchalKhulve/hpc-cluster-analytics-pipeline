import random
from datetime import datetime, timezone

from config.config import USERS, QUEUES

def generate_event():
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "job_id": random.randint(1000, 9999),
        "user": random.choice(USERS),
        "queue": random.choice(QUEUES),
        "cpu": random.randint(1, 16),
        "memory_gb": random.randint(4, 128),
        "runtime_sec": random.randint(10, 1000),
        "status": random.choice(["RUNNING", "SUCCESS", "FAILED"])
    }
