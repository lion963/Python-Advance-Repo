from collections import deque

pumps = int(input())
petrol_queue = deque()
distance_queue = deque()
fuel = 0
start_index = -1

for _ in range(pumps):
    petrol, distance = input().split()
    petrol = int(petrol)
    distance = int(distance)
    petrol_queue.append(petrol)
    distance_queue.append(distance)

while fuel <= 0:
    fuel = 0
    new_petrol_queue = petrol_queue.copy()
    new_distance_queue = distance_queue.copy()
    for i in range(pumps):
        if petrol_queue[i] >= distance_queue[i] and i > start_index:
            start_index = i
            break
        else:
            new_petrol_queue.popleft()
            new_petrol_queue.append(petrol_queue[i])
            new_distance_queue.popleft()
            new_distance_queue.append(distance_queue[i])

    for i in range(len(new_petrol_queue)):
        fuel += (new_petrol_queue[i] - new_distance_queue[i])
        if fuel < 0:
            break

print(start_index)
