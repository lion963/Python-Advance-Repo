from collections import deque

male_stack = list(map(int, input().split()))
female_queue = deque(list(map(int, input().split())))
matches = 0

while male_stack and female_queue:
    while True:
        if female_queue:
            if female_queue[0] <= 0:
                female_queue.popleft()
            else:
                break
        else:
            break

    while True:
        if male_stack:
            if male_stack[-1] <= 0:
                male_stack.pop()
            else:
                break
        else:
            break

    # equal checking
    if male_stack and female_queue:
        if male_stack[-1] == female_queue[0]:
            if not female_queue[0] % 25 == 0:
                matches += 1
                male_stack.pop()
                female_queue.popleft()
            else:
                matches += 1
                if len(female_queue) > 1:
                    female_queue.popleft()
                    female_queue.popleft()
                else:
                    female_queue.popleft()
                if len(male_stack) > 1:
                    male_stack.pop()
                    male_stack.pop()
                else:
                    male_stack.pop()
        else:
            if male_stack[-1] % 25 == 0:
                if len(male_stack) > 1:
                    male_stack.pop()
                    male_stack.pop()
                else:
                    male_stack.pop()
            else:
                male_stack[-1] -= 2
                if female_queue[0] % 25 == 0:
                    if len(female_queue) > 1:
                        female_queue.popleft()
                        female_queue.popleft()
                    else:
                        female_queue.popleft()
                else:
                    female_queue.popleft()

print(f'Matches: {matches}')
if male_stack:
    print(f'Males left: ', end='')
    print(*male_stack[::-1], sep=', ')
else:
    print(f'Males left: none')
if female_queue:
    print(f'Females left: ', end='')
    print(*female_queue, sep=', ')
else:
    print(f'Females left: none')
