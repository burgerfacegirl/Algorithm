# boj_1145_적어도 대부분의 배수_완전탐색

nums = list(map(int,input().split()))
ans = 0

for i in range(4, 1000001):
    cnt = 0
    for j in range(5):
        if i % nums[j] == 0:
            cnt += 1
    if cnt >= 3:
        ans = i
        break

print(ans)