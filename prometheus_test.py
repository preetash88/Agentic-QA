# prometheus_test.py

from prometheus_client import Counter, start_http_server
import time

c = Counter("test_counter", "A test counter")

print("Starting server...")
start_http_server(8000)
print("Server started")

while True:
    c.inc()
    print("Incremented")
    time.sleep(2)