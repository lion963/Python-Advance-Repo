vowels = ['a', 'o', 'u', 'e', 'i']
text = input()
text_without_vowels = [el for el in text if el not in vowels]
print(''.join(text_without_vowels))
