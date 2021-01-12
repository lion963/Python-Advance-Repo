from collections import deque

cars_queue = deque()

green_ligth = int(input())
free_window = int(input())
count = 0

while True:
    entering = green_ligth
    car = input()
    if car == 'END':
        break
    elif car == 'green':
        while cars_queue:
            if entering > 0:
                passing_car = cars_queue.popleft()
                entering -= len(passing_car)
                count += 1
            else:
                break
            if entering <= 0:
                if abs(entering) > free_window:
                    print(f'A crash happened!')
                    print(f'{passing_car} was hit at {passing_car[entering + free_window]}.')
                    quit()

    if not car == 'green' and not car == 'END':
        cars_queue.append((car))

print(f'Everyone is safe.')
print(f'{count} total cars passed the crossroads.')
