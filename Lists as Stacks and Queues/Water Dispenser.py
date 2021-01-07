from collections import deque

dispenser = int(input())
queue = deque()

while True:
    line = input()
    if line == 'Start':
        break
    else:
        queue.append(line)

while True:
    command = input()
    if command == 'End':
        print(f'{dispenser} liters left')
        break
    elif command[0].isdigit():
        liters = int(command)
        if liters > dispenser:
            print(f'{queue.popleft()} must wait')
        else:
            print(f'{queue.popleft()} got water')
            dispenser -= liters
    else:
        word, liters = command.split()
        liters = int(liters)
        dispenser += liters
