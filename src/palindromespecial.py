#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the substrCount function below.
def substrCount(n, s):
    # counting consective same characters
    l = []
    count = 1
    # reduce the 'asasd' into [(a, 1), (s, 1), (a, 1), (s, 1), (d, 1)]
    for i in range(1, n):
        if s[i - 1] == s[i]:
            count += 1
        else:
            l.append((s[i - 1], count))
            count = 1
    # capture last element
    l.append((s[n - 1], count))
    # count normal anagram, for example aaa can form 6 anagram ax3, aax2, aaax1
    count = 0
    for t in l:
        count += t[1] * (t[1] + 1) // 2
    # count special anagram
    for i in range(1, len(l) - 1):
        # special anagram's middle character will have a count of 1
        # also the left characters and right characters has to be the same
        # ex. aabaaa -> {aba, aabaa}
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            count += min(l[i - 1][1], l[i + 1][1])

    return count


if __name__ == '__main__':

    n = 3

    s = "aaaa"

    result = substrCount(n, s)

    print(f"{s} has {result} special palindromic substrings.")
