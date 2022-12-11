# Stack. 101773. Zero. silver 4

import sys
N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]
stack = []

for i in range(N):
    if arr[i] != 0:
        stack.append(arr[i])
    else:
        stack.pop()

print(sum(stack))