def factorize(n, c):
    a = list()
    for i in range(n-1):
        c -= 1
        a.append(1)
    a.append(1)
    for i in range(n-1):
        _c = min(n-i-1, c)
        if _c < 0:
            return [], -1
        c -= _c
        a[i] += _c
    return a, c


def solve(n, c):
    cost_array, cost_rem = factorize(n, c)
    if cost_rem != 0:
        return "IMPOSSIBLE"

    unknown = list()
    numbers = list()
    for i in range(0, n):
        unknown.append('?')
        numbers.append(i)

    for i in range(0, n):
        min_val = (i+1)
        j = i + cost_array[i] - 1
        unknown[numbers[j]] = min_val
        if i < (j+1):
            list_rev = numbers[i:(j+1)]
            list_rev.reverse()
            numbers = numbers[0:i] + list_rev + numbers[(j+1):n]

    return " ".join((str(e) for e in unknown))


t = int(input())
for i in range(1, t + 1):
    n, c = [int(s) for s in input().split(" ")]
    solution = solve(n, c)
    print("Case #{}: {}".format(i, solution))
