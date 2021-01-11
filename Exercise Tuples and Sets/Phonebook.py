tel_book = {}
names = []

while True:
    line = input()
    if not line.isdigit():
        name, phone = line.split('-')
        if name not in tel_book:
            tel_book[name] = phone
        tel_book[name] = phone
    else:
        n = int(line)
        break

for _ in range(n):
    name = input()
    if name in tel_book:
        print(f'{name} -> {tel_book[name]}')
    else:
        print(f'Contact {name} does not exist.')
