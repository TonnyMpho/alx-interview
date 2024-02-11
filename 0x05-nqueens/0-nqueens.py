#!/usr/bin/python3
""" 0. N queens """
import sys


def is_safe(board, row, col):
    """
    Check if there is a queen in the same row or diagonal
    """
    for prev_row, prev_col in board:
        if row == prev_row or col == prev_col or abs(
                row - prev_row) == abs(col - prev_col):
            return False
    return True


def solve_nqueens_util(board, col, n, solutions):
    """
    Recursive utility function to solve the N-Queens problem
    """
    if col == n:
        solutions.append(board.copy())
        return

    for row in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve_nqueens_util(board, col + 1, n, solutions)
            board.pop()


def solve_nqueens(n):
    """
    Solves the N-Queens problem and prints solutions.
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = []
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)

    for solution in solutions:
        print(solution)
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
