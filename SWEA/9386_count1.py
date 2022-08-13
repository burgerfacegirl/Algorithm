T = int(input())


for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    arr = list(map(int,input()))
    cnt_arr = []
    print(arr)
    for i in range(N):
        for j in range(N):
            if arr[j] == 1:
                cnt += 1
                if arr[j+1] ==1:
                    cnt += 1
                else:
                    cnt_arr.append(cnt)
                    cnt = 0
    print(cnt_arr)

