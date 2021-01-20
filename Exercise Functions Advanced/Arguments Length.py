def args_length(*args):
    count = 0
    for arg in args:
        count += 1
    return count


print(args_length(1, 32, 5))
print(args_length("john", "peter"))
print(args_length([1, 2, 3]))
