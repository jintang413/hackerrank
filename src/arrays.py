# Complete the hourglassSum function below.
def hourglassSum(arr):
    n = len(arr)
    max_sum = float('-inf')
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            cur_sum = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    cur_sum += arr[i+x][j+y]
            cur_sum -= (arr[i][j-1] + arr[i][j+1])
            if max_sum < cur_sum:
                max_sum = cur_sum
                print(i, j)
    return max_sum


# Complete the rotLeft function below.
def rotLeft(a, d):
    # Either a is None or a is one element return a
    if not a or len(a) == 1:
        return a

    # local new tail
    n = len(a)
    tail_idx = d % n
    return a[-(n - tail_idx):] + a[:tail_idx]


# Complete the minimumBribes function below.
def swap(i, j, arr):
    n = len(arr) - 1
    if i < 0 or j < 0 or i > n or j > n:
        raise IndexError("index out of range")

    arr[i], arr[j] = arr[j], arr[i]


def minimumBribes(q):
    num_bribes = 0

    for i in range(len(q), 0, -1):
        idx = i - 1
        if i != q[idx]:
            if i == q[idx - 1]:
                swap(idx, idx - 1, q)
                num_bribes += 1
            elif i == q[idx - 2]:
                swap(idx - 1, idx - 2, q)
                swap(idx, idx - 1, q)
                num_bribes += 2
            else:
                print("Too chaotic")
                return

    return num_bribes


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    if not arr or len(arr) == 1:
        return 0

    swaps = 0
    i = 0
    while i < len(arr):
        # ith index should store i+1
        if arr[i] != i + 1:
            # get the proper index for arr[i]
            j = arr[i] - 1
            # swap
            arr[j], arr[i] = arr[i], arr[j]
            swaps += 1
        else:
            i += 1

    return swaps


from collections import Counter


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    c = Counter()
    for a, b, k in queries:
        c[a] += k

        c[b + 1] -= k

    # the max b+1 should not be counted
    max_val = float("-inf")
    arr_sum = 0
    for i in sorted(c)[:-1]:
        arr_sum += c[i]
        max_val = arr_sum if arr_sum > max_val else max_val
    return max_val