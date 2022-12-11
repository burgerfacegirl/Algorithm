#221019_boj_11399_실버4

N = int(input())
time = list(map(int,input().split()))

time.sort()                 # 오름차순 정렬

ans = 0
K = 1

while True:
    for i in range(0, K):   # 정렬 된 리스트 누적합 구함 (최소 시간 구해야 하니까)
        ans += time[i]
    K += 1
    if K>N:
        break

print(ans)