# 220916_boj_2562_최댓값_구현_브론즈3

arr = [0] * 9

for i in range(9):
    n = int(input())
    arr[i] = n

maxV = max(arr)

for i in range(9):
    if arr[i] == maxV:
        print(maxV)
        print(i+1)