#220912_boj_1292_쉽게 푸는 문제_브론즈1

A, B = map(int,input().split())
# S = (1000*(1+1000))//2
arr = []

for i in range(50):
    for k in range(i):
        arr.append(i)

print(sum(arr[A-1:B]))

