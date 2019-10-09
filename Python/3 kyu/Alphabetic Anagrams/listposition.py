import numpy as np
from math import factorial
from decimal import Decimal
from collections import Counter


def listPosition(word):
    sorted_word = sorted(word)
    rank = 1
    
    for letter in word:
        if letter == sorted_word[0]:
            sorted_word.pop(0)
            continue
        else:
            pos = sorted_word.index(letter)
            rank += (pos * Decimal(factorial(len(sorted_word) - 1))) / np.prod(
                    [factorial(i) for i in Counter(sorted_word).values()])
            sorted_word.pop(pos)
    
    return int(rank)


if __name__ == '__main__':
    print(listPosition('A'))
    print(listPosition('ABAB'))
    print(listPosition('AAAB'))
    print(listPosition('BAAA'))
    print(listPosition('QUESTION'))
    print(listPosition('BOOKKEEPER'))
    print(listPosition('IMMUNOELECTROPHORETICALLY'))
