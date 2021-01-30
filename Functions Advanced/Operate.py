def operate(symbol, *args):
    num_list = [num for num in args]
    result = num_list[0]
    for i in range(1, len(num_list)):
        if symbol == '+':
            result += num_list[i]
        elif symbol == '-':
            result -= num_list[i]
        elif symbol == '*':
            result *= num_list[i]
        elif symbol == '/':
            result /= num_list[i]
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
