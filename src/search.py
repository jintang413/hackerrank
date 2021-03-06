def create_cost_index_map(cost):
    cost_index_map = {}
    for i in range(len(cost)):
        if cost[i] not in cost_index_map:
            cost_index_map[cost[i]] = [i]
        else:
            cost_index_map[cost[i]].append(i)
    return cost_index_map


def whatFlavors(cost, money):
    cost_index_map = create_cost_index_map(cost)

    for c in cost:
        remain_money = money - c
        count = len(cost_index_map.get(remain_money, [])) - 1
        if remain_money == c:
            count -= 1
        if count >= 0:
            if remain_money == c:
                l = cost_index_map[remain_money]
                x, y = l[0], l[1]
            else:
                x, y = cost_index_map[remain_money][0], cost_index_map[c][0]
            l = sorted([x + 1, y + 1])
            return l[0], l[1]


# Complete the pairs function below.
def pairs(k, arr):
    sum_set = set()
    number_set = set()
    for a in arr:
        sum_set.add(a + k)
        number_set.add(a)

    return len(sum_set.intersection(number_set))



# Complete the triplets function below.
# Key to this problem is to not reset the pq and qr counters
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    count = 0
    i = 0
    pq_count = 0
    qr_count = 0
    while i < len(b):

        while pq_count < len(a) and b[i] >= a[pq_count]:
            pq_count += 1

        while qr_count < len(c) and b[i] >= c[qr_count]:
            qr_count += 1

        count += pq_count * qr_count
        i += 1

    return count


# Complete the minTime function below.
def get_bounds(machines, goal):
    c = Counter(machines)
    fastest = min(c)
    return 1, math.ceil(fastest * goal / c[fastest]), c


def calculate_machines_produced(c, time):
    total_machines = 0
    for k, v in c.items():
        total_machines += (time // k) * v
    return total_machines


def minTime(machines, goal):
    lb, ub, c = get_bounds(machines, goal)
    print(lb, ub)
    while ub - lb > 1:
        mid = (lb + ub) // 2
        total_machines = calculate_machines_produced(c, time=mid)
        print(lb, ub, mid, total_machines)
        if total_machines < goal:
            lb = mid
        else:
            ub = mid
    return ub

# Complete the minTime function below.
def maximumSum(a, m):
    max_sum, mod_prefix= 0, 0
    a1=[]
    for i in a:
        mod_prefix = (mod_prefix + i) % m
        max_sum = max(max_sum, mod_prefix)
        ind = bisect.bisect_left(a1, mod_prefix + 1)
        if ind < len(a1):
            max_sum = max(max_sum, mod_prefix - a1[ind] + m)
        bisect.insort(a1, mod_prefix)
    return max_sum
