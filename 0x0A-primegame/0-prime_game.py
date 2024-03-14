#!/usr/bin/python3
""" 0x0A. Prime Game """


def primes(n):
    """Return list of prime numbers between 1 and n inclusive."""
    prime_numbers = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime_numbers.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime_numbers


def isWinner(x, nums):
    """
    Determines winner of Prime Game.
    """
    if x <= 0 or not nums:
        return None

    maria_wins = ben_wins = 0
    for n in nums:
        prime_numbers = primes(n)
        if len(prime_numbers) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    return None
