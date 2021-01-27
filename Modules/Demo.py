# import random
# fruits = ["apple", "banana", "cherry"]
#
# print(random.choice(fruits))
# print(random.randint(1, 10))
# random.shuffle(fruits)
# print(fruits)


from termcolor import colored
text = colored('Hello World!', 'red', attrs=['bold', 'underline'])
print(text)

from pyfiglet import figlet_format
text =figlet_format("Python",font="isometric1")
print(text)
