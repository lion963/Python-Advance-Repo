stack = list(map(int, input().split()))
capacity = int(input())
rack = 0
count = 0

while stack:
    while rack < capacity and stack:
        if rack + stack[-1] > capacity:
            break
        rack += stack.pop()
    if rack:
        count += 1
        rack = 0

print(count)
