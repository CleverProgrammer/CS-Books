"""
Author: Rafeh Qazi.
Project Euler Problem 11: https://projecteuler.net/problem=11
Description: Find the largest product of four consecutive numbers in the grid.
Constraints: None.
"""


def main():
    """
    The interface/signature of problem 11.
    """
    filename = 'problem_11_grid.txt'
    grid = text_to_grid(filename)
    product_of_rows()
    product_of_cols()
    product_of_diagonals()
    max_product()
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
    return


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
    :param args: list(s)
    :return: list
    """
