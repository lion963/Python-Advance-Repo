name_list = input().split()
toss = int(input())
count = 0
flag = True

removed_names = []

while len(name_list) > 1:
    if toss == 1:
        for i in range(len(name_list) - 1):
            print(f'Removed {name_list[i]}')
        print(f'Last is {name_list.pop()}')
        flag = False
        break
    else:
        for i in range(len(name_list)):
            count += 1
            if count % toss == 0:
                print(f'Removed {name_list[i]}')
                removed_names.append(name_list[i])

        for name in removed_names:
            name_list.remove(name)

        removed_names = []

if flag:
    print(f'Last is {name_list[0]}')
