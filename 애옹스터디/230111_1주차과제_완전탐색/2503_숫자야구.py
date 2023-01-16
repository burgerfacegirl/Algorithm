# boj_2503_숫자 야구_완전탐색

N = int(input())

answers = [list(map(int,input().split())) for _ in range(N)]

ans = 0
for i in range(123, 988):
    cnt = 0
    if str(i)[0] != str(i)[1] and str(i)[0] != str(i)[2] and str(i)[1] != str(i)[2] and '0' not in str(i):
        for j in range(N):
            s = 0
            b = 0
            for k in str(i):
                if k in str(answers[j][0]):
                    if str(i).index(k) == str(answers[j][0]).index(k):
                        s += 1
                    else:
                        b += 1
            if s == answers[j][1] and b == answers[j][2]:
                cnt += 1
            else:
                break
        if cnt == N:
            ans += 1

print(ans)
