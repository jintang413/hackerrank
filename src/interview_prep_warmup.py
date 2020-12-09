# Complete the sockMerchant function below.
def get_count_map(arr):
    count_map = {}
    for a in arr:
        count_map[a] = count_map.get(a, 0) + 1
    return count_map


def sockMerchant(n, ar):
    sock_count_map = get_count_map(ar)
    num_pairs = 0

    for k, v in sock_count_map.items():
        num_pairs += v // 2

    return num_pairs


def countingValleys(steps, path):
    # Write your code here
    num_valleys = 0
    prev_level = 0
    cur_level = 0
    for step in path:
        if step == "U":
            cur_level += 1
        elif step == "D":
            cur_level -= 1

        if cur_level == 0 and prev_level == -1:
            num_valleys += 1

        prev_level = cur_level

    return num_valleys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    jumps = 0
    i = 0
    while i < n:
        if (i + 2 == n - 1) or (i + 1 == n - 1):
            jumps += 1
            break
        if c[i + 2] == 1:
            i += 1
        else:
            i += 2
        jumps += 1
    return jumps


# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    a_counter = 0
    i = 0
    while i < l and i < n:
        if s[i] == "a":
            a_counter += 1
        i += 1

    if n < l:
        return a_counter
    else:
        m = n // l
        r = n % l
        i = 0
        a_counter = a_counter * m
        while i < r:
            if s[i] == "a":
                a_counter += 1
            i += 1

    return a_counter