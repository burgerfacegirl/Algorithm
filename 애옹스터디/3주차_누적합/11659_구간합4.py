# boj_11659

# import sys
# input = sys.stdin.readline
# N, M = input().split()
# nums = list(map(int,input().split()))
#
# for _ in range(int(M)):
#     a, b = map(int, input().split())
#     ans = 0
#     for i in range(a-1, b):
#         ans += nums[i]
#     print(ans)

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]  # init prefix_sum

temp = 0
for i in arr:  # accumulate arr section
    temp += i
    prefix_sum.append(temp)

for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
