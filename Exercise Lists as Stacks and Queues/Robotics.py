from collections import deque

robots_list = input().split(';')
hours, minutes, seconds = input().split(':')
hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)
robots_time = {}
products = deque()
second_count = 0
round = 0

for el in robots_list:
    robot, process_time = el.split('-')
    process_time = int(process_time)
    robots_time[robot] = ['available', process_time]

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    fist_product = products[0]
    round += 1
    for (robot, time) in robots_time.items():
        second_count += 1
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                hours += 1
                if hours == 23 and minutes == 60:
                    hours = 0
                minutes = 0
        if not time[0] == 'available':
            if time[0] % time[1] == 0:
                time[0] = 'available'
        if time[0] == 'available':
            if hours < 10:
                hours_str = '0' + str(hours)
            else:
                hours_str = str(hours)
            if minutes < 10:
                minutes_str = '0' + str(minutes)
            else:
                minutes_str = str(minutes)
            if seconds < 10:
                seconds_str = '0' + str(seconds)
            else:
                seconds_str = str(seconds)
            print(f'{robot} - {products.popleft()} [{hours_str}:{minutes_str}:{seconds_str}]')
        time[0] = second_count

    if products:
        if fist_product == products[0]:
            products.append(fist_product)
            products.popleft()
