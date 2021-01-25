# try:
#     text_file=open('text.txt', 'w')
#     print(f'File found')
# except FileNotFoundError:
#     print(f'File not found')

# try:
#     text_file=open('text.txt', 'r')
#     print(f'File found')
# except FileNotFoundError:
#     print(f'File not found')

# try:
#     text_file=open('D:\\text.txt', 'r')
#     print(f'File found')
# except FileNotFoundError:
#     print(f'File not found')

# print(text_file.readline())
# print(text_file.readlines())
# print(text_file.readline(5))
# print(text_file.read(2))
# print(text_file.read())

# lines=text_file.readlines()
# [print(line, end='') for line in lines]

# file = open("text.txt", 'r')
# for line in file:
#     print(line, end="")

# text_file.write("This is the write command.\n")
# text_file.write("It allows us to write in a particular file")
# text_file.close()

# file = open('python.txt', 'a')
# file.write("This is the write command.\n")
# file.write("It allows us to write in a particular file")
# file.close()

# file = open('python.txt', 'a')
# lines = ["Write ", "in ", "file"]
# file.writelines(lines)  # Write multiple strings
# file.close()

# with open("file.txt", "a") as f:
#     f.write("Hello World!!!")

# import os

# os.remove("python.txt")
# os.remove("D:\\text.txt")

# import os
# file_path = "file.txt"
# if os.path.exists(file_path):
#     os.remove(file_path)
