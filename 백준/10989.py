# 수 정렬하기3

N = int(input())
num_list = []
for i in range(N):
    num_list.append(int(input()))

num_list.sort()

for num in num_list:
    print(num)

10
5
2
3
1
4
2
3
5
1
7