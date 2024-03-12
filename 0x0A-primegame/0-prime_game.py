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
    """ Prime Game - winner function to determine the winner """

    def optimal_move(remaining):
        """
        Determines the optimal move for the current player.
        """
        for num in remaining:
            if is_prime(num):
                return num
        return None

    def play_game(n):
        """
        Simulates a single round of the game.
        """
        maria_turn = True
        rem_nums = list(range(1, n + 1))
        while True:
            prime = optimal_move(rem_nums)
            if prime is None:
                return not maria_turn
            rem_nums = [num for num in rem_nums if num % prime != 0]
            maria_turn = not maria_turn
            if not rem_nums:
                return maria_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
