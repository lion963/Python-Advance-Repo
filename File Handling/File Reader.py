sum = 0
file_num = open('numbers.txt', 'r')
for line in file_num:
    sum += int(line)

print(sum)
