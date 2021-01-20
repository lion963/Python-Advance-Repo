def even_num(a):
    if a % 2 == 0:
        return True
    return False


num_list = list(map(int, input().split()))
# num_list=list(filter(lambda x: (x%2==0), num_list))
num_list = list(filter(even_num, num_list))
print(num_list)