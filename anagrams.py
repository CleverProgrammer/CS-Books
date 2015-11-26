"""
Program: Anagram finder.
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
    all_words = dict()
    for word in word_list:
        word_count = dict()
        for ch in word:
            if ch not in word_count:
                word_count[ch] = 1
            else:
                word_count[ch] += 1
        all_words[word] = word_count

    for word in all_words:
        match = 0
        for other_word in all_words:
            if all_words[word] == all_words[other_word]:
                match += 1
                if match == 2:
                    anagrams.append(word)
                    break
    return sorted(anagrams)


def main():
    anagram_finder(['star', 'rats', 'cats', 'tacs', 'dog'])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
