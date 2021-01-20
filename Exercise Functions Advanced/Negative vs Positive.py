num_list = list(map(int, input().split()))
positives = list(filter(lambda x: (x > 0), num_list))
negatives = list(filter(lambda x: (x < 0), num_list))
print(sum(negatives))
print(sum(positives))
if abs(sum(negatives)) > sum(positives):
    print(f'The negatives are stronger than the positives')
else:
    print(f'The positives are stronger than the negatives')
