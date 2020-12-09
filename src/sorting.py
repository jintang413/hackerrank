# Bubble sort, count swaps
def countSwaps(a):
    num_swaps = 0
    n = len(a)
    for i in range(0, n):
        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1

    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n - 1]}")


# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(prices)
    toys = 0

    for p in prices:
        if k - p < 0:
            break
        k -= p
        toys += 1

    return toys

# custom comparator
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} {self.score}"

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name < b.name:
                return -1
            elif a.name > b.name:
                return 1
            else:
                return 0