#!/usr/bin/python3
"""Log Parsing"""

import sys

status_codes = {200, 301, 400, 401, 403, 404, 405, 500}
filesize = 0
statuscodeline = {}

count_line = 0


def print_metrics():
    """reads stdin line by line and computes metrics"""
    print(f"Total file size: {filesize}")

    for code in sorted(status_codes):
        count = statuscodeline.get(code, 0)
        if count > 0:
            print(f"{code}: {count}")

    print()
    reset_metrics()


def reset_metrics():
    """Resets metrics"""
    global filesize, statuscodeline
    filesize = 0
    statuscodeline = {}


try:
    for line in sys.stdin:
        count_line += 1

        parts = line.split()
        if len(parts) != 10 or parts[5] != '"GET' or parts[6] != '/projects/260':
            continue

        status_code, file_size = int(parts[8]), int(parts[9])

        filesize += file_size

        if status_code in status_codes:
            statuscodeline[status_code] = statuscodeline.get(
                status_code, 0) + 1

        if count_line % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    print_metrics()
