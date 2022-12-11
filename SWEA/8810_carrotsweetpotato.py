# SWEA_추가문제_8810_당근밭옆고구마밭

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    potato = list(map(int,input().split()))
    j = 0
    # j_sum = 0
    j_list = []
    for i in range(N-1):
        check = 0
        if potato[i+1] > potato[i]:
            check = 1
            j_list.append(i)
        if potato[i-1] < potato[i]:
            if check :
                j += 1
        if check and i == N-1:
            j += 1


    print(j+1, j_list)

    # for i in range(len(j_list)):
