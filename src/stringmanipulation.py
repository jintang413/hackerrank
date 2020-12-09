from collections import Counter

# Complete the makeAnagram function below.
def createCountMap(arr):
    count_map = {}
    for a in arr:
        count_map[a] = count_map.get(a, 0) + 1
    return count_map


def makeAnagram(a, b):
    a_count_map = createCountMap(a)
    b_count_map = createCountMap(b)
    deletions = 0
    for k in a_count_map:
        deletions += abs(a_count_map[k] - b_count_map.get(k, 0))
        if k in b_count_map:
            del b_count_map[k]

    for k in b_count_map:
        deletions += b_count_map[k]

    return deletions


# Complete the alternatingCharacters function below.
def alternatingCharacters(word):
    deletions = 0
    for i in range(0, len(word) - 1):
        if word[i] == word[i + 1]:
            deletions += 1
    return deletions


# Sherlock considers a string to be valid if all characters of the string appear the same number of times.
# It is also valid if he can remove just 1 character at 1 index in the string,
# and the remaining characters will occur the same number of times.
# Given a string s, determine if it is valid. If so, return YES, otherwise return NO.
# Complete the isValid function below.
def isValid(s):
    freq_counter = Counter(s)
    unique_freq_counter = Counter(freq_counter.values())
    if len(unique_freq_counter) == 1:
        return "YES"
    elif len(unique_freq_counter) == 2:
        key1, key2 = unique_freq_counter.keys()
        if unique_freq_counter[key1] == 1 and (key1 - 1 == key2 or key1 - 1 == 0):
            return "YES"
        elif unique_freq_counter[key2] == 1 and (key2 - 1 == key1 or key2 - 1 == 0):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

# A string is said to be a special string if either of two conditions is met:

# All of the characters are the same, e.g. aaa.
# All characters except the middle one are the same, e.g. aadaa.
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


# A string is said to be a child of a another string if it can be formed by deleting 0 or more characters
# from the other string. Given two strings of equal length, what's the longest string that can be constructed
# such that it is a child of both?
def lcs_recursive(s1, s2, m, n):

    if m == 0 or n == 0:
        return 0
    # if the last elements are equal
    elif s1[m-1] == s2[n-1]:
        return 1 + lcs_recursive(s1, s2, m - 1, n - 1)
    else:
        # reduce s1 by one element
        c1 = lcs_recursive(s1, s2, m - 1, n)
        # reduce s2 by one element
        c2 = lcs_recursive(s1, s2, m, n - 1)
        return max(c1, c2)


def lcs_dp(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in range(m + 1)]

    """Following steps build L[m + 1][n + 1] in bottom up fashion 
    Note: L[i][j] contains length of LCS of X[0..i-1] 
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

                # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]
