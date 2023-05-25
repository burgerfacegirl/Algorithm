N = int(input())

for i in range(N):
    ans = 'YES'
    num = int(input())

    for j in range(2, 10**6+1):
        if num % j == 0:
            ans = 'NO'
            break
    print(ans)