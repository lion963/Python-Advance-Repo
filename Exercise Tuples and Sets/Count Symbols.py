text = input()

letters_list = []

for char in text:
    letters_list.append(char)

letters_list.sort()
letters = tuple(letters_list)
letters_set = sorted(set(letters))

for char in letters_set:
    print(f'{char}: {letters.count(char)} time/s')
