"""
Author: Rafeh Qazi.
Project Euler Problem 11: https://projecteuler.net/problem=11
Description: Find the largest product of four consecutive numbers in the grid.
Constraints: Grid has to be a square.
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
    for row in grid:
        last_idx = len(row) - 1
        for idx, _ in enumerate(row):
            if idx == last_idx:
                continue
            current_four = row[idx: idx + 4]
            product_of_four = reduce(mul, current_four)
            if product_of_four > result:
                result = product_of_four
                biggest = current_four
    return biggest


def cols_to_rows(grid):
    """
    Takes a grid and returns all the columns as a 2d list of rows.
    :param grid: list
    :return: list
    """
    cols = []
    col_idx = 0
    while col_idx != len(grid[0]):
        temp = []
        for row in grid:
            temp.append(row[col_idx])
        col_idx += 1
        cols.append(temp)
    return cols


def product_of_cols(grid):
    """
    Takes a grid and returns the top 4 consecutive products in a col.
    :param grid: list
    :return: list
    """
    return product_of_rows(cols_to_rows(grid))

def diag_rows_to_rows(grid):
    """
    Takes a grid as input. Converts all horizontal starting diagonals to rows.
    :param grid: list
    :return: list
    """
    pass

def product_of_diagonals(grid):
    """
    Takes a grid and returns the top 4 consecutive products in a diagonal.
    :param grid: list
    :return: list
    """
    # all row diagonals
    # all column diagonals
    # diagonal to rows
    # product of rows
    diags_rows = []
    i = 0
    for idx, row in enumerate(grid):
        try:
            print(row, i)
            print(row[i])
            diags_rows.append(row[idx])
            print(diags_rows)
            i += 1
        except IndexError:
            i = 0
            continue
    return


def max_product(*args):
    """
    Takes a list of products and returns the result of the list with the greatest
    product.
    :param args: list
    :return: float
    """
    # biggest = []
    greatest_product = 0
    for _list in args:
        result = reduce(mul, _list)
        if result > greatest_product:
            # biggest = _list
            greatest_product = result
    return greatest_product
