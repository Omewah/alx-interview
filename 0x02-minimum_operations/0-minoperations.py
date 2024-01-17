#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Analyze the fewest number of ops to result in n H characters"""
    if n <= 1:
        return 0

    ops_num = [float('inf')] * (n + 1)
    ops_num[1] = 0

    for i in range(2, n+1):
        for j in range(1, i):
            if i % j == 0:
                ops_num[i] = min(ops_num[i], ops_num[j] + 1 // j)

    return ops_num[n] if ops_num[n] != float('inf') else 0
