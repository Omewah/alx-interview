#!/usr/bin/python3
"""UTF-8 Validation"""


def get_bit_set(num):
    """Returns the bit sets"""
    bitset = 0
    helper = 1 << 7
    while helper & num:
        bitset += 1
        helper = helper >> 1
    return bitset


def validUTF8(data):
    """Checks if the data is UTF-8 encoded"""
    counterB = 0
    for i in range(len(data)):
        if counterB == 0:
            counterB = get_bit_set(data[i])

            if counterB == 0:
                continue
            if counterB == 1 or counterB > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        counterB -= 1
    return counterB == 0
