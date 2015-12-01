"""
Author: Rafeh Qazi.
A highly divisble triangular number.
"""


def triangular_divisibilities(n_divisors):
    """
    Return the first triangular number with n_divisors.
    :param n_divisors: int
    :return: int
    >>> triangular_divisibilities(5)
    28
    >>> triangular_divisibilities(6)
    36
    """
    factors = []
    number = 1
    counter = 1
    while len(factors) <= n_divisors:
        number = arithmetic_sum(counter)
        factors = all_factors(number, n_divisors)
        counter += 1
    return number


def arithmetic_sum(n):
    """
    Takes as input the nth term and returns
    the result of the summation from 1..nth number.
    :param n: float
    :return: int
    >>> arithmetic_sum(10)
    55
    """
    return int(n * (n + 1) / 2)


def all_factors(n, _max):
    """
    and returns after max iterations.
    Takes as input a number and returns all its factors. Stops
    :param n: int
    :param _max: int
    :return: list
    >>> all_factors(3, 3)
    [3, 1]
    >>> all_factors(n=6, _max=21)
    [6, 1, 2, 3]
    >>> all_factors(28, 6)
    [28, 1, 2, 4, 7, 14]
    """
    factors = [n]
    for num in range(1, (n + 2) // 2):
        if len(factors) > _max:
            break
        elif n % num == 0:
            factors.append(num)
    return factors


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import time
    start = time.time()
    triangular_divisibilities(150)
    print('It took {0:0.7f} seconds to run first test'.format(time.time() - start))
