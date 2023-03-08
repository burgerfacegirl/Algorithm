import sys

N = int(sys.stdin.readline())

cards = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

nums = list(map(int,sys.stdin.readline().split()))
check_minus = [0] * 10000001
check_plus = [0] * 10000001

for i in range(N):
    if cards[i] >= 0:
      check_plus[cards[i]] += 1
    else:
        check_minus[abs(cards[i])] += 1


for j in range(M):
    if nums[j] >= 0:
        if check_plus[nums[j]] > 0:
            nums[j] = check_plus[nums[j]]
        else:
            nums[j] = 0
    else:
        if check_minus[abs(nums[j])] > 0:
            nums[j] = check_minus[abs(nums[j])]
        else:
            nums[j] = 0

for num in nums:
    print(num, end=' ')