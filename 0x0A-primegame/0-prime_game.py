#!/usr/bin/python3
""" 0x0A. Prime Game """


def is_prime(num):
    """
    Helper function to check if a number is prime.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """
    Determines the winner of each game based on the rules described.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        maria_turn = True
        while n > 1:
            prime = 2
            while prime <= n:
                if is_prime(prime):
                    break
                prime += 1

            if prime > n:
                if maria_turn:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break
            n -= prime * (n // prime)
            maria_turn = not maria_turn
        
        if n == 1:
            if maria_turn:
                ben_wins += 1
            else:
                maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
