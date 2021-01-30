word_list = [x for x in input().split(', ')]
length_words = {word: len(word) for word in word_list}
list1 = []
for key, value in length_words.items():
    list1.append(str(key) + ' -> ' + str(value))
print(', '.join(list1))
