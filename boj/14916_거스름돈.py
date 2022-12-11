# 220926_boj_14916_거스름돈_실버5

N = int(input())
ans = 0
# while N > 0:
#     if N % 5 == 0:
#         ans = N//5
#     elif N % 5 == 2:
#         ans = N//5 + (N%5)//2
#     elif N % 5

while True:
    if N % 5 == 0:
        ans += N//5
        break
    else:
        N -= 2
        ans += 1
    if N < 0 and N % 5 != 0:
        ans = -1
        break

print(ans)