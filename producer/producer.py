import logging
import time

from producer.event_generator import generate_event
from config.config import EVENT_INTERVAL

logging.basicConfig(level=logging.INFO)

while True:
    event = generate_event()

    logging.info(event)

    time.sleep(EVENT_INTERVAL)
