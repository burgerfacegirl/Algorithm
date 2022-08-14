#수 이어쓰기 - string으로 하면 시간초과

N = int(input())
cnt = 0

digit = len(str(N))
# sq = digit -1

for i in range(digit, 0, -1):
    sq = i - 1
    if i == digit:
        cnt = cnt + i * (N - 10 ** sq + 1)
    else:
        cnt = cnt + i * ((10 ** i) - (10 ** sq))
    
print(cnt)