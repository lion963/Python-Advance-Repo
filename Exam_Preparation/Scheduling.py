from collections import deque

jobs = list(map(int, input().split(', ')))
needed_index = int(input())
cycles = 0
flag = True
indexes = []

while flag:
    min_cycle = 1000000
    for i in range(len(jobs)):
        if jobs[i] < min_cycle and i not in indexes:
            min_cycle = jobs[i]
            index = i

    if index == needed_index:
        flag = False
    indexes.append(index)
    cycles += min_cycle

print(cycles)
