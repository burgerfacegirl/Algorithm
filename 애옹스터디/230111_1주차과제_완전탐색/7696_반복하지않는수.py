# boj_7696_반복하지 않는 수_완전탐색
import sys
import test


L = []
while True:
    n = int(sys.stdin.readline())
    L.append(n)
    if n == 0:
        break

nums = [0] * (max(L)+1)
for i in range(1, 10):
    nums[i] = i
i = 0
ho = 10
ni = 1
idx = 1
nimax = 9
while idx <= max(L):
    if nimax < ni:
        if int(str(i)[0]) != 9:
            ni = 0
            i += ho
        else:
            ho *= 10
            i = ho
            nimax = idx
            ni = 0

    check = i+nums[ni]
    if sorted(list(set(str(check)))) == sorted(list(str(check))):
        nums[idx] = check
        idx += 1
        # print(check)
    ni += 1

for l in L:
    if l == 0:
        break
    print('nums : ', nums)
    print('시간초과 :', test.nums)
