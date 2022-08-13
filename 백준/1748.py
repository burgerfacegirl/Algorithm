N = int(input())
cnt = 9

digit = len(str(N))
sq = digit -1

while N >= 10:
    cnt = cnt + digit * (N - 10 ** sq + 1)
    N = N - ((N // (10 ** sq)) * (10 ** sq))
    digit -= 1

print(cnt)