def add_nums(list, *args):
    if args[0] == 'beginning':
        list = [num for num in args[1:]] + list
    elif args[0] == 'end':
        for num in args[1:]:
            list.append(num)
    return list


def remove_nums(list, *args):
    if len(args) == 1:
        if args[0] == 'beginning':
            list = list[1:]
        elif args[0] == 'end':
            list.pop()
    else:
        if args[0] == 'beginning':
            for i in range(args[1]):
                list = list[1:]
        elif args[0] == 'end':
            for i in range(args[1]):
                list.pop()
    return list


def list_manipulator(list, *args):
    num_list = list
    if args[0] == 'add':
        num_list = add_nums(num_list, *args[1:])
    elif args[0] == 'remove':
        num_list = remove_nums(num_list, *args[1:])
    return num_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
