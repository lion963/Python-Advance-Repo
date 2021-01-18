list_char = list(input().split(', '))

char_dict = {el: ord(el) for el in list_char}
print(char_dict)
