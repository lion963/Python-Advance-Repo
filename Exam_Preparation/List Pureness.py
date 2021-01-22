def best_list_pureness(*args):
    import sys
    num_list = args[0]
    k = args[1]
    best_sum = -sys.maxsize
    if k == 0:
        sum = 0
        for j in range(len(num_list)):
            sum += num_list[j] * j
            if sum > best_sum:
                best_sum = sum
                rotation = 0
    else:
        for i in range(k + 1):
            sum = 0
            for j in range(len(num_list)):
                sum += num_list[j] * j
            if sum > best_sum:
                best_sum = sum
                rotation = i
            num_list = num_list[-1:] + num_list[:-1]
    return f'Best pureness {best_sum} after {rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
