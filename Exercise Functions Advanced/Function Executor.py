def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    functions_list = [el[0] for el in args]
    tuple_list = [el[1] for el in args]
    result_list = []
    for i in range(len(functions_list)):
        result = functions_list[i](*tuple_list[i])
        result_list.append(result)
    return result_list


# def func_executor(*args):
#     result_list = []
#     for el in args:
#         result_list.append(el[0](*el[1]))
#     return result_list


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
