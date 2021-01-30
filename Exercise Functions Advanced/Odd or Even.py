def odd(list1):
    odd_nums = list(filter(lambda x: (x % 2 != 0), list1))
    sum_odd = sum(odd_nums) * len(list1)
    return sum_odd


def even(list1):
    even_nums = list(filter(lambda x: (x % 2 == 0), list1))
    sum_even = sum(even_nums) * len(list1)
    return sum_even


command = input()
num_list = list(map(int, input().split()))

if command == 'Odd':
    print(odd(num_list))
elif command == 'Even':
    print(even(num_list))
