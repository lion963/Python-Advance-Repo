n = int(input())

set_cars = set()

for _ in range(n):
    direction, car = input().split(', ')
    if direction == 'IN':
        set_cars.add(car)
    elif direction == 'OUT':
        set_cars.discard(car)

if set_cars:
    for el in set_cars:
        print(el)
else:
    print(f'Parking Lot is Empty')
