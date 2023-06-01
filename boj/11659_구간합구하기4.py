N, M = map(int, input().split())
nums = list(map(int, input().split()))

# accumulated_sum = [nums[0]] + [0] * (N-1)
#
for i in range(1, N):
    nums[i] = nums[i-1] + nums[i]

for i in range(M):
    s, l = map(int, input().split())
    s, l = s-1, l-1
    if s == 0:
        print(nums[l])
    else:
        print(nums[l] - nums[s-1])
