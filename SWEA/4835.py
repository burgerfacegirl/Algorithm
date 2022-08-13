import sys
sys.stdin = open('4835.txt')


T = int(input())

for tc in range(1, T+1):
    arr = list(map(int,input().split())) # N,M = map(int,input().split())으로 바로 받아올 수 있음.
    num_list = list(map(int,input().split()))
    N = arr[0]
    M = arr[1]
    sum_list = []
    for i in range(len(num_list)-M+1):
        M_list = num_list[i:i+M]
        sum = 0
        for j in range(len(M_list)):
            sum += M_list[j]
        sum_list.append(sum)
    maxV = minV = sum_list[0]
    for num in range(len(sum_list)):
        if maxV < sum_list[num]:
            maxV = sum_list[num]
        if minV > sum_list[num]:
            minV = sum_list[num]
    print(f'#{tc} {maxV-minV}')