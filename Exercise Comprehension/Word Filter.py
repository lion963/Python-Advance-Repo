word_list = [x for x in input().split()]
even_word_list = [word for word in word_list if len(word) % 2 == 0]
print(*even_word_list, sep='\n')
