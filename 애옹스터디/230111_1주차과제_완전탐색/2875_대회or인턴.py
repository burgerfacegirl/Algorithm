# boj_2875_대회 or 인턴

# N = 여학생 수, M = 남학생 수, K = 인턴쉽에 참여해야 하는 인원

N, M, K = map(int, input().split())

team = 0

while True:
    N = N - 2
    M = M - 1
    if N < 0 or M < 0 or N+M<K:
        break
    else:
        team += 1

print(team)