#!/usr/bin/env python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):  # Adjust the range if you want fewer lines
    sleep(random.uniform(0.1, 1.0))  # Add a delay to simulate real-time logging
    # Format each log line
    log_line = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    )
    sys.stdout.write(log_line)
    sys.stdout.flush()
