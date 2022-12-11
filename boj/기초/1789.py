# 수들의 합


N = int(input())
s = 0
for i in range(1,N+1):
    s = s + i
    if s > N:
        print(i-1)
        break
    elif s == N:
        print(i)
        break