#!/usr/bin/python3
"""A script that solves the N-Queens problem using backtracking."""

import sys


def solve_n_queens(n):
    """Solve the N-Queens problem using backtracking."""
    solutions = []
    # Each index represents a row, value represents the column position of the
    # queen
    board = [-1] * n
    place_queen(board, 0, n, solutions)
    return solutions


def place_queen(board, row, n, solutions):
    """Recursively place queens on the board."""
    if row == n:  # All queens are placed successfully
        solutions.append([[i, board[i]] for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place the queen
            # Recurse for the next row
            place_queen(board, row + 1, n, solutions)
            board[row] = -1  # Backtrack


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i] == col or abs(
                board[i] -
                col) == abs(
                i -
                row):  # Same column or diagonal
            return False
    return True


if __name__ == "__main__":
    # Input validation
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print solutions
    solutions = solve_n_queens(n)
    for solution in solutions:
        print(solution)
