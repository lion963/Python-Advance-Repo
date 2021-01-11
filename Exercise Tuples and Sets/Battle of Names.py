import math

n = int(input())
odd_nums = set()
even_nums = set()

for i in range(1, n + 1):
    name = input()
    sum_char = 0

    for char in name:
        sum_char += ord(char)
    sum_char = math.floor(sum_char / i)

    if sum_char % 2 == 0:
        even_nums.add(sum_char)
    else:
        odd_nums.add(sum_char)

if sum(odd_nums) == sum(even_nums):
    print(*odd_nums.union(even_nums), sep=', ')
elif sum(odd_nums) > sum(even_nums):
    print(*odd_nums.difference(even_nums), sep=', ')
elif sum(odd_nums) < sum(even_nums):
    print(*odd_nums.symmetric_difference(even_nums), sep=', ')
