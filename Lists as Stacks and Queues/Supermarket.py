from collections import deque

queue = deque()

while True:
    line = input()

    if line == 'Paid':
        while len(queue):
            print(queue.popleft())
    elif line == 'End':
        print(f'{len(queue)} people remaining.')
        break
    else:
        queue.append(line)
