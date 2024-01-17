#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Analyze the fewest number of ops to result in n H characters"""
    if not isinstance(n, int):
        return 0

    ops_num = 0
    dbase = 0
    currH = 1

    while currH < n:
        if dbase == 0:
            dbase = currH
            currH += dbase
            ops_num += 2
        elif n - currH > 0 and (n - currH) % currH == 0:
            dbase = currH
            currH += dbase
            ops_num += 2
        elif dbase > 0:
            currH += dbase
            ops_num += 1
    return ops_num
