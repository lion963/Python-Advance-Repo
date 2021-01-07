text = input()
stack = []

for i in range(len(text)):
    stack.append(text[i])
stack = stack[::-1]

print(''.join(stack))
