from collections import deque
from datetime import datetime, timedelta

data = input().split(';')
time = datetime.strptime(input(), '%H:%M:%S')

robots = []
available_robots = deque([])
products = []

for el in data:
    robot_data = el.split('-')
    robot = {}
    robot['name'] = robot_data[0]
    robot['processing_time'] = int(robot_data[1])
    robot['available_at'] = time
    robots.append(robot)
    available_robots.append(robot)

product = input()
available_robots = deque(available_robots)
while not product == "End":
    products.append(product)
    product = input()

products = deque(products)
time = time + timedelta(seconds=1)

while len(products) > 0:
    current_product = products.popleft()

    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
        print (f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r['available_at']:
                available_robots.append(r)
        if not available_robots:
            products.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = time + timedelta(seconds=current_robot['processing_time'])
            print (f"{robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    time = time + timedelta(seconds=1)


# from collections import deque
#
# robots_list = input().split(';')
# hours, minutes, seconds = input().split(':')
# hours = int(hours)
# minutes = int(minutes)
# seconds = int(seconds)
# robots_time = {}
# products = deque()
# second_count = 0
# round = 0
#
# for el in robots_list:
#     robot, process_time = el.split('-')
#     process_time = int(process_time)
#     robots_time[robot] = ['available', process_time]
#
# while True:
#     product = input()
#     if product == 'End':
#         break
#     products.append(product)
#
# while products:
#     fist_product = products[0]
#     round += 1
#     for (robot, time) in robots_time.items():
#         second_count += 1
#         seconds += 1
#         if seconds == 60:
#             seconds = 0
#             minutes += 1
#             if minutes == 60:
#                 hours += 1
#                 if hours == 23 and minutes == 60:
#                     hours = 0
#                 minutes = 0
#         if not time[0] == 'available':
#             if time[0] % time[1] == 0:
#                 time[0] = 'available'
#         if time[0] == 'available':
#             if hours < 10:
#                 hours_str = '0' + str(hours)
#             else:
#                 hours_str = str(hours)
#             if minutes < 10:
#                 minutes_str = '0' + str(minutes)
#             else:
#                 minutes_str = str(minutes)
#             if seconds < 10:
#                 seconds_str = '0' + str(seconds)
#             else:
#                 seconds_str = str(seconds)
#             print(f'{robot} - {products.popleft()} [{hours_str}:{minutes_str}:{seconds_str}]')
#         time[0] = second_count
#
#     if products:
#         if fist_product == products[0]:
#             products.append(fist_product)
#             products.popleft()
