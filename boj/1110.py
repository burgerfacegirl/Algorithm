N = input()

if int(N) < 10:
    N = '0' + N

cnt = 0
newN = 0
hi = True
K = N
while hi:
    newN = int(N)//10 + int(N)%10
    N = str(int(N)%10) + str(newN%10) 
    cnt += 1
    if N == K:
        hi = False
print(cnt)
