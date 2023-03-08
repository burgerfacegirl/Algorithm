# boj_7696_반복하지 않는 수_완전탐색
import sys

nums = [0] * (1000001)
i = 1
idx = 1
while idx <= 1000000:
    check = []
    d = 10
    k = i
    while(k>0):
        check.append(k%d)
        k = k//d

    if len(set(check)) == len(check):
        nums[idx] = i
        idx += 1
    i += 1


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(nums[n])