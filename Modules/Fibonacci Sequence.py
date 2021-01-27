from Modules.test_modules.fibonacci_sequence import *

while True:
    line = input()
    if line == 'Stop':
        break
    if 'Create' in line:
        command, word, number = line.split()
        number = int(number)
        fib_list = fibonacci_seq(number)
        print(*fib_list, sep=' ')

    elif 'Locate' in line:
        command, num = line.split()
        num = int(num)
        print(fibonacci_locate(fib_list, num))
