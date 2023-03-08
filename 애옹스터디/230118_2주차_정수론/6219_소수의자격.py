# boj_6219_소수의 자격_정수론

A, B, D = map(int, input().split())

ans = 0
for i in range(A, B+1):
    cnt = 0
    for j in range(2, int(i**0.5)+1):
        if i%j == 0 or i == 1:
            cnt += 1
            break
    if cnt == 0:
        if str(D) in str(i):
            ans += 1

print(ans)