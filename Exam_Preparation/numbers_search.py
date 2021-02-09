def find_min_num(numbers):
    return min(numbers)


def find_max_num(numbers):
    return max(numbers)


def find_miss_nums(min_n, max_n, numbers):
    miss_num = []
    for num in range(min_n, max_n + 1):
        if num not in numbers:
            miss_num.append(num)
    return miss_num


def find_duplicates(numbers):
    nums_count = {}
    for num in numbers:
        if num not in nums_count:
            nums_count[num] = 1
        else:
            nums_count[num] += 1
    duplicates = [key for key, value in nums_count.items() if value > 1]
    return sorted(duplicates)


def numbers_searching(*args):
    result = []
    min_num = find_min_num(args)
    max_num = find_max_num(args)
    result.extend(find_miss_nums(min_num, max_num, args))
    result.append(find_duplicates(args))
    return result

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))