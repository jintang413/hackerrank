from collections import Counter


# Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
def sherlockAndAnagrams(s):
    buckets = {}
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            key = frozenset(Counter(s[i : i + j]).items())  # O(N) time key extract
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key] - 1) // 2
    return count


def createCountMap(arr):
    count_map = {}
    for i in arr:
        if i not in count_map:
            count_map[i] = 1
        else:
            count_map[i] += 1
    return count_map


# Ransom Note, Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    magazine_count_map = createCountMap(magazine)

    for word in note:
        if word not in magazine_count_map:
            return "No"
        else:
            magazine_count_map[word] -= 1
            if magazine_count_map[word] < 0:
                return "No"
    return "Yes"

# Given two strings, determine if they share a common substring. A substring may be as small as one character.
def twoStrings(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)
    return "YES" if set_s1.intersection(set_s2) else "NO"

# You are given an array and you need to find number of tripets of indices
# such that the elements at those indices (i, j, k) are in geometric progression
# for a given common ratio r and i < j < k.
def countTriplets(arr, r):
    n = len(arr)
    count = 0
    pairs_map = {}
    count_map = {}
    for i in range(n - 1, -1, -1):
        x = arr[i]
        x_r = x * r
        x_r_r = x * r * r

        # case if x is the first element
        count += pairs_map.get((x_r, x_r_r), 0)

        # case if x is the second element
        pairs_map[(x, x_r)] = pairs_map.get((x, x_r), 0) + count_map.get(x_r, 0)

        # case if x is the third element
        count_map[x] = count_map.get(x, 0) + 1

    return count


# Complete the freqQuery function below.
# You are given  queries. Each query is of the form two integers described below:
# 1: Insert x in your data structure.
# 2: Delete one occurence of y from your data structure, if present.
# 3: Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.
def freqQuery(queries):
    # key is the value and value is the frequency
    count_map = {}
    freq_map = {}
    res = []
    for q_action, x in queries:
        if q_action == 1:
            old_freq, new_freq = insert_count_map(count_map, x)
            updateFrequencyMap(freq_map, old_freq, new_freq)
        elif q_action == 2:
            old_freq, new_freq = delete_count_map(count_map, x)
            updateFrequencyMap(freq_map, old_freq, new_freq)
        elif q_action == 3:
            res.append(checkFreqPresent(freq_map, x))
    return res


def updateFrequencyMap(freq_map, old_freq, new_freq):
    if old_freq:
        freq_map[old_freq] -= 1
    if new_freq:
        freq_map[new_freq] = freq_map.get(new_freq, 0) + 1


def insert_count_map(count_map, x):
    old_freq = count_map.get(x, 0)
    count_map[x] = count_map.get(x, 0) + 1
    return old_freq, count_map[x]


def delete_count_map(count_map, x):
    if x in count_map:
        old_freq = count_map[x]
        count_map[x] -= 1
        if count_map[x] == 0:
            del count_map[x]
        return old_freq, count_map.get(x)
    else:
        return None, None


def checkFreqPresent(freq_map, f):
    freq_val = freq_map.get(f, 0)
    return 1 if freq_val > 0 else 0
