# 220929_boj_14501_퇴사_실버3
# def plan(i, p):
#     while True:
#         p = p+P[i]
#         if i + T[i] - 1 > N:            # 예전날짜+걸리는 날(시작하는 날)이 남은 N일보다 크면 새로운 날로 안가고 반복문 종료
#             break
#         i = i+T[i]
#         if i > N:
#             break
#         if i + T[i] - 1 > N:            # 새로운 날짜+걸리는 날-1(끝나는 날)이 남은 N일보다 크면 반복문 종료
#             break
#     return p

def plan(i, p):
    while True:
        p = p + P[i]
        if i + T[i] - 1 > N:
              break
        i = i+T[i]
        if i > N:
            break
        if i + T[i] - 1 > N:            # 새로운 날짜+걸리는 날-1(끝나는 날)이 남은 N일보다 크면 반복문 종료
            break
    profits.append(p)

N = int(input())
# schedule = [[] for _ in range(N+1)]
can = []
T = [0] * (N+1)
P = [0] * (N+1)

for i in range(1, N+1):
    Ti, Pi = map(int,input().split())
    T[i] = Ti
    P[i] = Pi
    profits = []

for i in range(1, N+1):
    if i + T[i] - 1 <= N:
        profits.append(plan(i, 0))

print(profits)
print(max(profits))

