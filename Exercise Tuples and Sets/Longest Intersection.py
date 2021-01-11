n = int(input())
set1 = set()
set2 = set()
max_set = set()

for _ in range(n):
    set1.clear()
    set2.clear()
    nums1, nums2 = input().split('-')
    range1 = list(map(int, nums1.split(',')))
    range2 = list(map(int, nums2.split(',')))

    for i in range(range1[0], range1[1] + 1):
        set1.add(i)
    for i in range(range2[0], range2[1] + 1):
        set2.add(i)

    new_set = set1.intersection(set2)

    if len(new_set) > len(max_set):
        max_set = new_set

print(f'Longest intersection is', [el for el in max_set], f'with length {len(max_set)}')
