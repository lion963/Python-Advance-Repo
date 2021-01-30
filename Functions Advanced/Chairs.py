def calc_combinations(names, n, combs=[]):
    if len(combs) == n:
        print(", ".join(combs))
        return

    for i in range(len(names)):
        name = names[i]
        combs.append(name)
        calc_combinations(names[i+1:], n, combs)
        combs.pop()


names = input().split(", ")
n = int(input())

calc_combinations(names, n)


# from itertools import combinations
# name_list=input().split(', ')
# n=int(input())
# comb = combinations(name_list, 2)
# for el in comb:
#     print(', '.join(el))

# def combinations(list, n, combos=[]):
#     if combos is None:
#         combos = []
#     if len(list) == n:
#         if combos.count(list) == 0:
#             combos.append(list)
#             print(', '.join(list))
#             # combos.sort()
#         return combos
#     else:
#         for i in range(len(list)):
#             refined_list = list[:i] + list[i + 1:]
#             combos = combinations(refined_list, n, combos)
#         return combos
#
#
# name_list = input().split(', ')
# n = int(input())
#
# combinations(name_list, n)

