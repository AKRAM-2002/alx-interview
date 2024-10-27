#!/usr/bin/env python3
"""
Write a script that reads stdin line by line and computes metrics
"""

import re
import sys
import signal


total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}
line_count = 0


def print_metrics():
    """Print the metrics for total file size and status codes."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle the SIGINT signal (CTRL + C)."""
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    match = re.match(
        r'(\d{1,3}(?:\.\d{1,3}){3}) - \[.*?\] "GET .*?" (\d{3}) (\d+)',
        line)
    if match:
        _, status_code, file_size = match.groups()
        file_size = int(file_size)

        # Update total size and status code counts
        total_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_metrics()


print_metrics()
