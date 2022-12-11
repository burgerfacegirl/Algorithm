ans = 0
bingo_r = bingo_c = bingo_x = 0

x = [list(map(int,input().split())) for _ in range(5)]
bingo = [list(map(int,input().split())) for _ in range(5)]

for i in range(5):
    for j in range(5):
        for p in range(5):
            for q in range(5):
                if bingo[p][q] == x[i][j]:
                    bingo[p][q] = 0
                    ans += 1
            bingo_r = bingo_c = bingo_x = 0
            for k in range(5):
                for h in range(5):
                    if bingo[k][h] == 0:
                        bingo_r += 1
                    if bingo[h][k] == 0:
                        bingo_c += 1
                    if bingo[k][k] == 0:
                        bingo_x += 1
            if bingo_c == 5 or bingo_r == 5 or bingo_x ==5:
                print(ans)
#             if bingo_r == 5 :
#                 ans += 1
#             if bingo_x == 5 :
#                 ans += 1
# print(ans)