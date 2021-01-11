sets_1_2 = tuple(map(int, input().split()))
set1 = set()
set2 = set()

for _ in range(sets_1_2[0]):
    set1.add(input())

for _ in range(sets_1_2[1]):
    set2.add(input())

unique_el = set1.intersection(set2)
for el in unique_el:
    print(el)
