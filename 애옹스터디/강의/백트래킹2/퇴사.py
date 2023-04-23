def recur(cur, total):
    global ans
    if cur > n:
        return

    if cur == n:
        ans = max(ans, total)
        return
    recur(cur+arr[cur][0], total+arr[cur][1])
    recur(cur+1, total)

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
recur(0)

print(ans)

# 최적화 시켜야 하는 문제
# 현재 cur일
# 앞으로 일을 최선을 다해 고를 때, 얼마를 벌 수 있는지 리턴
# ex. recur(4) 는 35 리턴

# 일반적인 DP => 바텀업 dp --> 다음주에
# 탑다운 dp => 메모이제이션
# 1. 진입장벽이 높다 => 백트래킹 중하수
# 2. 실버 문제나 골드 문제나 체감 난이도 차이가 없이 풀 수 있다.
# 익숙해지면 DP = 백트래킹
def recur(cur, total):
    global ans
    if cur > n:
        return -1000000

    if cur == n:
        return 0 # 남은 날짜 없어서 앞으로 벌 수 있는 돈 더 없으니까 0 리턴

    if dp[cur] != -1: # 초기값이 아니라 구해본 값이라면 return 해주겠다
       return dp[cur]
    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    return dp[cur]

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
dp = [-1 for i in range(n)]

# 해당일에 벌 수 있는 최대 돈은 그날 일을 했을때(일해서 버는돈 + 몇일 후 벌수 있는 최대 돈) 벌 수있는 돈과 그날 일을 안했을 때 벌 수 있는 돈(다음날 벌 수 있는 최대돈) 중 최대
# ex.
# 현재가 5일이면 최대한 버는 돈
# recur(5 + arr[5][0]) + arr[cur][1]) 그날 일 했을때
# recur(5 + 1)  그날 일 안했을때 // 둘 중 더 큰거

# 7일 이후에 일을 안해야 되는데, 이걸 '일을 안한다' 대신에 '일을 하면 큰 손해를 본다'로 바꾼 느낌이네요
# 구현 팁임
# if 문 걸어주는 대신에 -100000 리턴해서 큰 손해를 보게 만드는거

# 근데 그 초기값에서 값을 구할 때 왜 7에서부터 가는건가요..!? 그 앞에는 뒤에 일도 더해줘서 그런건가요..?
# 이 문제가 뒤에 걸 알아야 앞에 걸 알 수 있는 형태




