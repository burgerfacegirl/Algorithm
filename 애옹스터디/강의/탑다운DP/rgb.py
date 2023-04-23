n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

def recur(cur, total, prv):
    global ans

    if ans == n:
        ans = min(ans, total)
        return

    for i in range(3):
        if i == prv:
            continue

        recur(cur + 1, total + arr[cur][i], [i])

'''
탑 다운 DP 짜는법
1. 백트래킹을 짠다.
2. 리턴하는 방식으로 바꾼다(처음부터 이렇게 짜도 무방.)
3. 공식 대입
'''

def recur(cur, prv):
    if cur == n:
        return 0

    # 메모이제이션
    if dp[cur][prv] != -1:
        return dp[cur][prv]
    
    ret = 10000000
    for i in range(3):
        if i == prv:
            continue

        ret = min(recur(cur+1, i) + arr[cur][i])

    # 메모이제이션
    dp[cur][prv] = ret

    return ret

dp = [[-1 for i in range(3)] for j in range(n)]
print(recur(0, -1))