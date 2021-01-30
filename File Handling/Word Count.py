import re

pattern = r'\w+'

line = open('words.txt', 'r')
text = open('text.txt', 'r')
words = re.findall(pattern, line.read())

found_word = []
for word in words:
    pattern = r'(?<=\s|-)' + word
    found_word.append(re.findall(pattern, open('text.txt', 'r').read(), re.IGNORECASE))

found_word = sorted(found_word, key=lambda x: -len(x))

for el in found_word:
    print(f'{el[0].lower()} - {len(el)}')
