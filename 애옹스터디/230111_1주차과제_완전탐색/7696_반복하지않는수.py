# boj_7696_반복하지 않는 수_완전탐색
import sys
from itertools import permutations

T = 1000000
nums = list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 1)) + list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 2)) + list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 3)) +list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 4)) + list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 5)) + list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 6))
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(10, 987655):
#     j = str(i)
#     if len(str(i)) == 2:
#         if j[0] != j[1]:
#             nums += [i]
#     elif len(str(i)) == 3:
#         if j[0] != j[1] and j[0] != j[2] and j[1] != j[2]:
#             nums += [i]
#     elif len(str(i)) == 4:
#         if j[0] != j[1] and j[0] != j[2] and j[0] != j[3] and j[1] != j[2] and j[1] != j[3] and j[2] != j[3]:
#             nums += [i]
#     elif len(str(i)) == 5:
#         if j[0] != j[1] and j[0] != j[2] and j[0] != j[3] and j[0] != j[4] and j[1] != j[2] and j[1] != j[3] and j[1] != j[4] and j[2] != j[3] and j[2] != j[4] and j[3] != j[4]:
#             nums += [i]
#     elif len(str(i)) == 6:
#         if j[0] != j[1] and j[0] != j[2] and j[0] != j[3] and j[0] != j[4] and j[0] != j[5] and j[1] != j[2] and j[1] != j[3] and j[1] != j[4] and j[1] != j[5] and j[2] != j[3] and j[2] != j[4] and j[2] != j[5] and j[3] != j[4] and j[3] != j[5] and j[4] != j[5]:
#             nums += [i]

for i in range(len(nums)):
    nums[i] = int(''.join(nums[i]))

nums = sorted(list(set(nums)))
for tc in range(T):
    n = int(input())
    if n == 0:
        break
    else:
        print(nums[n])
