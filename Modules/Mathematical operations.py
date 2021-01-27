from Modules.test_modules.mathematical_operations import *

list_arg = input().split()
num1 = float(list_arg[0])
num2 = int(list_arg[2])
operator = list_arg[1]

print(f'{math_operations(operator, num1, num2):.2f}')
