
# 백트래킹
# 시간초과나옴
def recur(cur, w, total):
    global ans
    if w > m:
        return
    if cur == n:
        ans = max(ans,total)
        return
    recur(cur+1, w+arr[cur][0], total+arr[cur][1])
    recur(cur+1, w, total)

# total은 return 값으로 빠질 거임
# 앞으로 최대 얼만큼의 가치를 얻을 수 있냐
# return 하는 방식로 바꾸기
def recur(cur, w):
    # 퇴사 문제랑 같은 이유 / 잘못온거 판별해줌
    if w > m:
        return -100000000

    if cur == n:
        return 0

    return max(recur(cur+1, w+arr[cur][0]) + arr[cur][1], recur(cur + 1, w))


# 메모이제이션 추가
def recur(cur, w):
    # 퇴사 문제랑 같은 이유 / 잘못온거 판별해줌
    if w > m:
        return -100000000

    if cur == n:
        return 0

    if dp[cur][w] != -1:
        return dp[cur[w]]

    dp[cur][w] = max(recur(cur + 1, w + arr[cur][0]) + arr[cur][1], recur(cur + 1, w))
    return dp[cur][w]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [[-1 for i in range(10010)] for j in range(n)]
ans = 0

print(recur(0,0))

# 탑다운과 다음에 배울 바텀업이랑 시간차이/메모리차이는 많이 나나요?
# 파이썬은 탑다운 거의 못 쓸 정도로 많이남

# 다음주에 탑다운 코드를 바텀업으로 바꾸는 방법 배움
# 한단계만 더 추가하면됨
# recur(cur, w)는 dp[cur][w]과 완전히 같은 값
# dp[cur][w] = max(dp[cur+1][w+arr[cur][0]] + arr[cur][1], dp[cur+1][j])