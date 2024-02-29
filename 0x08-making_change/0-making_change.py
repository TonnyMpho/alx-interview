#!/usr/bin/python3
""" Change comes from within
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    new_total = total

    for coin in coins:
        num_coins = new_total // coin
        count += num_coins
        new_total -= num_coins * coin

    return count if new_total == 0 else -1
