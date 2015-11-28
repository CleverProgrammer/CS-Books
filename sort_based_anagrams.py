"""
Author: Rafeh Qazi.
Program: Anagram Finder.
Description: Return a sorted list with all non-anagrams omitted.
Constraints: No imports.
input: anagram_finder(['star', 'rats', 'cats', 'tacs', 'dog'])
output: ['cats', 'rats', 'star', 'tacs']
"""


def anagram_finder(word_list):
    """
    :param word_list: list
    :return: list
    >>> anagram_finder(['star', 'rats', 'cats', 'tacs', 'dog'])
    ['cats', 'rats', 'star', 'tacs']
    >>> anagram_finder(['ox', 'box'])
    []
    >>> anagram_finder(['ox', 'xo', 'caracer', 'racecar'])
    ['caracer', 'ox', 'racecar', 'xo']
    """
    anagrams = []
    for word in word_list:
        match = 0
        for other_word in word_list:
            if sorted(word) == sorted(other_word):
                match += 1
                if match == 2:
                    anagrams.append(word)
    return sorted(anagrams)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import time
    start_time = time.time()
    anagram_finder(['star', 'rats', 'cats', 'tacs', 'dog'])
    print('it took {0:.6f} seconds to run.'.format(time.time() - start_time))
