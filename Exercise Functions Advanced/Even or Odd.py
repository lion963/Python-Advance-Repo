def even_odd(*args):
    inputs = [el for el in args]
    command = inputs.pop()
    if command == 'even':
        num_list = list(filter(lambda x: x % 2 == 0, inputs))
    elif command == 'odd':
        num_list = list(filter(lambda x: x % 2 != 0, inputs))
    return num_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
