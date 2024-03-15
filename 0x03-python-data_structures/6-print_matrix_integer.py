#!/usr/bin/python3

def print_matrix_integer(matrix=[]):
    """Print a matrix of integers."""
    for row in matrix:
        for i, value in enumerate(row):
            print("{:d}".format(value), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print("")
