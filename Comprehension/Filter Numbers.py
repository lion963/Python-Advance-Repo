num1 = int(input())
num2 = int(input()) + 1

numbers = [num for num in range(num1, num2)]
nums_list = [num for num in numbers if any([num % ele == 0 for ele in range(2, 11)])]
print(nums_list)
