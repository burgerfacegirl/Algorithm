# 홀수만 더하기

for tc in range(1,int(input())+1):
    arr = list(map(int,input().split()))
    s = 0
    for i in range(len(arr)):
        if arr[i]%2:
            s += arr[i]
    print(f'#{tc} {s}')