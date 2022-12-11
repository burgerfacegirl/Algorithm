#221019_boj_24091_퀵 정렬2_실버5

import sys
sys.setrecursionlimit(10000)

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q-1)
        quick_sort(arr, q+1, r)


def partition(arr, p, r):
    global cnt
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            cnt += 1
            if cnt == K:
                print(*arr)
    if i+1 != r :
        arr[i+1], arr[r] = arr[r], arr[i+1]
        cnt += 1
        if cnt == K :
            print(*arr)
    return i + 1


N, K = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0

quick_sort(arr, 0, N-1)
# print(cnt)

if cnt < K:
    print(-1)
