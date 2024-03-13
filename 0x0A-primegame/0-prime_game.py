#!/usr/bin/python3
"""The Prime Game"""


def check_prime(n):
    """will check if n is a prime number """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def add_prime(n, primes):
    """this will Add the prime n to list"""
    addprime = primes[-1]
    if n > addprime:
        for i in range(addprime + 1, n + 1):
            if check_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """Returns the name of the player with the most wins"""

    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    add_prime(max(nums), primes)

    for round in range(x):
        roundsum = sum((i != 0 and i <= nums[round])
                       for i in primes[:nums[round] + 1])
        if (roundsum % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
