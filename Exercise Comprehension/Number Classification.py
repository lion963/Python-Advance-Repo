numbers = [int(x) for x in input().split(', ')]
positive = [num for num in numbers if num >= 0]
negative = [num for num in numbers if num < 0]
even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if not num % 2 == 0]
print(f'Positive: ', end='')
print(*positive, sep=', ')
print(f'Negative: ', end='')
print(*negative, sep=', ')
print(f'Even: ', end='')
print(*even, sep=', ')
print(f'Odd: ', end='')
print(*odd, sep=', ')
