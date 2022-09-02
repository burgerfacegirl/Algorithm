# 17608. 막대기 (stack, bronze2)

N = int(input())

arr = list(int(input()) for _ in range(N))
right = []
cnt = 0
for i in range(N-1, 0, -1):
    last = arr.pop()
    right.append(last)
    for j in range(len(right)):
        if right[j] > last:
            cnt += 1
print(cnt)