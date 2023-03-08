# boj_1978_소수 찾기_정수론

N = int(input())
nums = list(map(int, input().split()))

ans = 0
for i in range(N):
    cnt = 0
    for j in range(2, int(nums[i]**0.5) + 1):
        if nums[i] % j == 0:
            cnt += 1
    if cnt == 0 and nums[i] != 1:
        ans += 1
print(ans)