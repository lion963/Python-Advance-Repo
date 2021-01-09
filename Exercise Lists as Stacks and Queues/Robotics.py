from collections import deque

robots_list = input().split(';')
hours, minutes, seconds = input().split(':')
hours = int(hours)
minutes = int(minutes)
seconds = int(seconds)
robots_time = {}
products = deque()
second_count=0

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
    second_count+=1
    fist_product=products[0]
    for robot, value in robots_time.items():
        if value[0] == 'available':
            print(f'{robot} - {products.popleft()} [time]')
            value[0]='busy'
        if value[1]%second_count==0:
            value[0]='available'
    if fist_product==products[0]:
        products.append(fist_product)
        products.popleft()


