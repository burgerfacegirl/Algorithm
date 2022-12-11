# Stack_10828_스택_silver4

import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    n = sys.stdin.readline()
    if 'push' in n:
        push_x = n.split()
        x = int(push_x[-1])
        stack.append(x)
    elif n == 'top\n':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif n == 'size\n':
        print(len(stack))
    elif n == 'empty\n':
        if stack:
            print(0)
        else:
            print(1)
    elif n == 'pop\n':
        if stack:
            y = stack.pop()
            print(y)
        else:
            print(-1)

