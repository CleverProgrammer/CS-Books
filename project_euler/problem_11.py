"""
Author: Rafeh Qazi.
Project Euler Problem 11: https://projecteuler.net/problem=11
Description: Find the largest product of four consecutive numbers in the grid.
Constraints: None.
"""
from functools import reduce
from operator import mul


def main():
    """
    The interface/signature of problem 11.
    """
    filename = 'problem_11_grid.txt'
    grid = text_to_grid(filename)
    row_prod = product_of_rows(grid)
    col_prod = product_of_cols(grid)
    diag_prod = product_of_diagonals(grid)
    max_prod = max_product(row_prod, col_prod, diag_prod)
    print(max_prod)
    pass


def text_to_grid(filename):
    """
    Convert a text grid to a 2d grid of class list.
    :param filename: string
    :return: list
    """
    with open(filename, 'r') as f:
        return [list(map(int, line.strip().split())) for line in f]


def product_of_rows(grid):
    """
    Takes a grid and returns the top 4 consecutive products in a row.
    :param grid: list
    :return: list
    """
    biggest = []
    result = 0
    last_idx = len(grid[0]) - 1
    for idx, _ in enumerate(grid[0]):
        if idx != last_idx:
            return biggest
        current_four = grid[0][idx: idx + 4]
        if reduce(mul, current_four) > result:
            biggest = current_four
    return biggest


def product_of_cols(grid):
    """
    Takes a grid and returns the top 4 consecutive products in a col.
    :param grid: list
    :return: list
    """
    return


def product_of_diagonals(grid):
    """
    Takes a grid and returns the top 4 consecutive products in a diagonal.
    :param grid: list
    :return: list
    """
    return


def max_product(*args):
    """
    Takes a list of products and returns the list with the max product.
    :param args: list
    :return: list
    """
    biggest = []
    current_product = 0
    for _list in args:
        if reduce(mul, _list) > current_product:
            biggest = _list
    return biggest
