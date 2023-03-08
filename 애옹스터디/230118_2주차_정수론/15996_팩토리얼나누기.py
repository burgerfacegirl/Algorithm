# boj_15996_팩토리얼 나누기

N, A = map(int, input().split())

count = 0
X = A
while X <= N:
    count += N // X
    X *= A
print(count)