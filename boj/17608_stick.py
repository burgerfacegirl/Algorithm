# 17608. 막대기 (stack, bronze2)

import sys
# N = int(input())
# arr = []
# for _ in range(N):
#     arr.append(int(input()))
#
# maxH = 0
# cnt = 0
# for i in range(N):
#     num = arr.pop()
#     if num > maxH:
#         cnt += 1
#         maxH = num
# print(cnt)


# right_list = []
# cnt = 1
# top = N-1
# for i in range(N-2, -1, -1):
#     last = arr[top]
#     right_list = arr[top:N]
#     top -= 1
#     cnt_r = 0
#     for j in range(len(right_list)):
#         if arr[i] <= right_list[j]:
#             cnt_r = -1
#     if cnt_r != -1:
#         cnt += 1

# cnt = 1
# for i in range(N-1):
#     maxV = max(arr[i+1:N])
#     if arr[i] > maxV :
#         cnt += 1

# print(cnt)

import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

maxH = 0
cnt = 0
for i in range(N):
    num = arr.pop()
    if num > maxH:
        cnt += 1
        maxH = num
print(cnt)