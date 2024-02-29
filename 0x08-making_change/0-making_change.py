#!/usr/bin/python3
"""Making Change Problem"""


def make_change(coins, total):
    """Checks the fewest number of coins needed to meet total"""
    if total <= 0:
        return 0

    curr_total = 0
    old_coin_val = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total - curr_total) // coin
        curr_total += r * coin
        old_coin_val += r
        if curr_total == total:
            return old_coin_val
    return -1
