"""
Author: Rafeh Qazi.
A highly divisble triangular number.
# TODO: Binary search for all_factors.
1. increase number by the power of 2
2. If the len(factors) is > _max
3. Reduce by power of 2 and check again.
4 if len(factors) is still > _max.
5. repeat step 3 and 4.
6. If len(factors) < _max.
7. Now we have the min and max range of numbers our solution is bounded by.
8. Increase numbers incrementally at this p
"""


def main():
    """
    The interface/signature of the entire program.
    """
    # Call arithmetic sum on N numbers to collect their result.
    # Put this result in a list.
    # If index of the result matches the n_divisors parameter,
    # then return that number.
    # ============= A more specific algorithm. ===============
    # 1. n = arithmetic_sum(1)
    # 2. factors = all_factors(n)
    # 3. If len(factors) == n_divisors then return True.
    pass


def triangular_divisibilities(n_divisors):
    """
    Return the first triangular number with n_divisors.
    :param n_divisors: int
    :return: int
    # >>> triangular_divisibilities(5)
    28
    # >>> triangular_divisibilities(6)
    36
    """
    # terms = [arithmetic_sum(i + 1) for i in range(n_divisors)]
    # print(terms)
    # factors = [all_factors(i + 1) for i in range(n_divisors)]
    # print(factors)
    factors = []
    number = 1
    counter = 1
    while len(factors) < n_divisors:
        number = arithmetic_sum(counter)
        # print('stuff:', number)
        # print('counter:', counter, '-->', factors, '| current num:', number)
        factors = all_factors(number, n_divisors)
        counter += 1
        # print('factors:', len(factors), '-->', factors)
        # print(sum(range(number + 1)))
        print(counter)
    # print('stuff:', number)
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
    # >>> all_factors(3, 3)
    # [1, 3]
    # >>> all_factors(6, _max=21)
    # [1, 2, 3, 6]
    # >>> all_factors(28, 6)
    # [1, 2, 4, 7, 14, 28]
    """
    # print('all_factors({0}, {1})'.format(n, _max))
    factors = [n]
    # print('range:', list(range(1, (n + 2) // 2)))
    # print('max tries:', _max)
    for num in range(1, (n + 2) // 2):
        if len(factors) > _max:
            # print('breaking')
            break
        elif n % num == 0:
            factors.append(num)
            # print(factors)
            # print('-->', factors, '| current num:', num)
    return factors


# def fg(n):
    # yield (i for i in range(1, n + 1) if n % i == 0)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(triangular_divisibilities(6))
    print(triangular_divisibilities(200))
    # solutiion for td(200)
    # factors = [i for i in range(1, 2031121) if 2031120 % i == 0]
