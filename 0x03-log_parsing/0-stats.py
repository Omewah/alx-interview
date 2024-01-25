#!/usr/bin/python3
"""Log Parsing"""
import dis
import sys


def display_metrics(totalsize, statuscode):
    """Function that print the metrics"""

    print('File size: {}'.format(totalsize))
    for key, value in sorted(statuscode.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


if __name__ == '__main__':
    totalsize = 0
    statuscode = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    try:
        i = 0
        for line in sys.stdin:
            args = line.split()
            if len(args) > 6:
                status = args[-2]
                filesize = args[-1]
                totalsize += int(filesize)
                if status in statuscode:
                    i += 1
                    statuscode[status] += 1
                    if i % 10 == 0:
                        display_metrics(totalsize, statuscode)

    except KeyboardInterrupt:
        display_metrics(totalsize, statuscode)
        raise
    else:
        display_metrics(totalsize, statuscode)
