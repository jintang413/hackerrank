# Complete the countInversions function below.
def countInversions(arr):
    # arr is empty or null
    if not arr:
        return arr
    # arr is one element
    if len(arr) == 1:
        return arr

    left, right = 0, len(arr) - 1

    return merge_sort(arr, left, right)


def merge_sort(arr, left, right):
    inversions = 0
    if left >= right:
        return inversions

    mid = (left + right) // 2
    # print(f"left: {arr[left:mid+1]}, right: {arr[mid+1:right+1]}")
    inversions += merge_sort(arr, left, mid)
    inversions += merge_sort(arr, mid + 1, right)
    inversions += merge(arr, left, right)

    return inversions


def merge(arr, left, right):
    inversions = 0
    mid = (left + right) // 2
    l, s, r = 0, left, 0
    arr_left = arr[left : mid + 1]
    arr_right = arr[mid + 1 : right + 1]
    while l < len(arr_left) and r < len(arr_right):
        if arr_left[l] <= arr_right[r]:
            arr[s] = arr_left[l]
            l += 1
        else:
            arr[s] = arr_right[r]
            r += 1
            inversions += len(arr_left) - l
        s += 1

    while l < len(arr_left):
        arr[s] = arr_left[l]
        l += 1
        s += 1

    while r < len(arr_right):
        arr[s] = arr_right[r]
        r += 1
        s += 1
    return inversions


if __name__ == "__main__":

    t = [[1, 1, 1, 2, 2], [2, 1, 3, 1, 2]]

    for arr in t:
        result = countInversions(arr)
        print(result)
