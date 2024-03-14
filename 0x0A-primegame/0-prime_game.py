#!/usr/bin/python3
""" 0x0A. Prime Game """


def sieve_of_eratosthenes(limit):
    """ sieve algorithm """
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False

    for num in range(int(limit ** 0.5) + 1, limit + 1):
        if sieve[num]:
            primes.append(num)

    return primes

def isWinner(x, nums):
    """ Function to determine if a number is prime """
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        """ Function to play the game for a given round and n """
        primes = sieve_of_eratosthenes(n)
        primes_set = set(primes)
        turn = 0

        while True:
            if turn == 0:
                # Maria's turn
                for prime in primes:
                    if prime <= n and prime in primes_set:
                        primes_set -= {i for i in range(prime, n + 1, prime)}
                        turn = 1
                        break
                else:
                    return "Ben"
            else:
                # Ben's turn
                for prime in primes:
                    if prime <= n and prime in primes_set:
                        primes_set -= {i for i in range(prime, n + 1, prime)}
                        turn = 0
                        break
                else:
                    return "Maria"

    winners = {"Maria": 0, "Ben": 0}

    for i in range(x):
        winner = play_game(nums[i])
        winners[winner] += 1

    max_wins = max(winners.values())
    if list(winners.values()).count(max_wins) > 1:
        return None
    else:
        return max(winners, key=winners.get)
