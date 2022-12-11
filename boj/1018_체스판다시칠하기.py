#221019_boj_1018_체스판다시칠하기_실버4


N, M = map(int,input().split())
chess_pan = [list(input()) for _ in range(N)]
change = []

for a in range(N-7):
    for b in range(M-7):
        B = 0       # 맨 왼쪽 위가 검은색일때 다시 칠해야 하는 정사각형의 수
        W = 0       # 맨 왼쪽 위가 흰색일때 다시 칠해야 하는 정사각형의 수
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if chess_pan[i][j] != 'W':
                        W += 1
                    else:
                        B += 1
                else:
                    if chess_pan[i][j] != 'W':
                        B += 1
                    else:
                        W += 1
        change.append(min(B, W))

print(min(change))
