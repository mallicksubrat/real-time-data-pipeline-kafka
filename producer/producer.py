from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

EVENTS = ["click", "view", "purchase", "scroll"]
PAGES = ["/home", "/product", "/checkout", "/search"]

def generate_event():
    return {
        "user_id": random.randint(1, 1000),
        "event_type": random.choice(EVENTS),
        "page": random.choice(PAGES),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    event = generate_event()
    producer.send("test-topic", event)
    print("Sent:", event)
    time.sleep(1)

