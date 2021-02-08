def check_time(customer, taxi):
    if taxi >= customer:
        return True
    return False


def print_result(customers, taxis):
    if not customers:
        return f'All customers were driven to their destinations\nTotal time: {total_time} minutes'
    return f'Not all customers were driven to their destinations\nCustomers left: {", ".join(map(str, customers))}'


from collections import deque

customers_queue = deque(list(map(int, input().split(', '))))
taxis_stack = list(map(int, input().split(', ')))

total_time = 0

while customers_queue and taxis_stack:
    if check_time(customers_queue[0], taxis_stack[-1]):
        total_time += customers_queue.popleft()
        taxis_stack.pop()
    else:
        taxis_stack.pop()

print(print_result(customers_queue, taxis_stack))
