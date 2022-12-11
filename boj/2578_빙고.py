def bingo():
    global check
    check = 0
    for i in range(5):
        check_r = check_c = 0
        for j in range(5):
            if pan[j][i] == 0:                # 열 확인
                check_c += 1
            if pan[i][j] == 0:                # 행 확인
                check_r += 1
        if check_r == 5:
            check += 1
        if check_c == 5:
            check += 1

    check_x_l = 0                             # 정대각선 확인
    for i in range(5):
        if pan[i][i] == 0:
            check_x_l += 1
    if check_x_l == 5:
        check += 1

    check_x_r = 0                             # 역대각선 확인
    for i in range(5):
        if pan[i][4-i] == 0:
            check_x_r += 1
    if check_x_r == 5:
        check += 1



pan = [list(map(int,input().split())) for _ in range(5)]        # 빙고 판
x = []
for i in range(5):                                              # 사회자가 부르는 숫자 1차원 배열로 받기
    x += list(map(int,input().split()))
# print(x)

check = 0
a = 0                                                           # for문 중단을 위한 변수
ans = 0
for k in range(25):
    for i in range(5):
        for j in range(5):
            if pan[i][j] == x[k]:
                pan[i][j] = 0
                ans += 1
                if k > 10:                                      # 빙고 3줄 되려면 적어도 11개 이상 불러야 됨
                    bingo()
                    if check >= 3:
                        a = 1
                        break
            if a==1:
                break
        if a == 1:
            break
    if a == 1:
        break


print(ans)


# print(pan)







# ans = 0
# bingo_r = bingo_c = bingo_x = 0
# for i in range(5):
#     for j in range(5):
#         for p in range(5):
#             for q in range(5):
#                 if bingo[p][q] == x[i][j]:
#                     bingo[p][q] = 0
#                     ans += 1
#             bingo_r = bingo_c = bingo_x = 0
#             for k in range(5):
#                 for h in range(5):
#                     if bingo[k][h] == 0:
#                         bingo_r += 1
#                     if bingo[h][k] == 0:
#                         bingo_c += 1
#                     if bingo[k][k] == 0:
#                         bingo_x += 1
#             if bingo_c == 5 or bingo_r == 5 or bingo_x ==5:
#                 print(ans)
#             if bingo_r == 5 :
#                 ans += 1
#             if bingo_x == 5 :
#                 ans += 1
# print(ans)