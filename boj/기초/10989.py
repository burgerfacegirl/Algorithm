# 수 정렬하기3

N = int(input())
num_list = [0] * N

for i in range(N):
    num_list[i] = int(input())

num_list.sort()

for num in num_list:
    print(num)

