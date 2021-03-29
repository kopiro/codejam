def solve(numbers):
    len_nums = len(numbers)
    cost = 0
    for i in range(0, len_nums-1):
        slice_nums = numbers[i:len_nums]
        min_num = min(slice_nums)
        min_num_index = i + slice_nums.index(min_num) + 1
        cost = cost + (min_num_index-i)
        list_rev = numbers[i:min_num_index]
        list_rev.reverse()
        numbers = numbers[0:i] + list_rev + numbers[min_num_index:len_nums]
    return cost


t = int(input())
for i in range(1, t + 1):
    size = int(input())
    numbers = [int(s) for s in input().split(" ")]
    solution = solve(numbers)
    print("Case #{}: {}".format(i, solution))
