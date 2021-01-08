brakets = list(input())
stack = []

for braket in brakets:
    if braket == '{' or braket == '[' or braket == '(':
        stack.append(braket)
    else:
        if stack:
            if braket == '}' and stack.pop() == '{':
                pass
            elif braket == ']' and stack.pop() == '[':
                pass
            elif braket == ')' and stack.pop() == '(':
                pass
            else:
                break
        else:
            print(f'NO')
            quit()

if not stack:
    print(f'YES')
else:
    print(f'NO')
