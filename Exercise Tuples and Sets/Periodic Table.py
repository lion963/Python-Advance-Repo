n = int(input())

unique_el = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        unique_el.add(el)

for el in unique_el:
    print(el)
