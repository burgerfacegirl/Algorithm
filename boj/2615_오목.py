# boj_2615_오목


pan = [list(map(int,input().split())) for _ in range(19)]

check = False

# di = [0, 1, 1,1]
# dj = [1, 1, 0,-1]

di = [-1, 0, 1,1]
dj = [1, 1, 1,0]

for j in range(19):
    for i in range(19):
        if pan[i][j] == 1:
            for k in range(4):
                cnt_b = 1
                si, sj = i, j
                while True:
                    ni, nj = i+di[k], j+dj[k]
                    if 0<=ni<19 and 0<=nj<19 and pan[ni][nj] == 1:
                        cnt_b += 1
                        i, j = ni, nj
                    else:
                        i, j = si, sj
                        break
                if cnt_b == 5:
                    if pan[si-di[k]][sj-dj[k]] != 1:
                        # if k == 3:
                        #     print(1)
                        #     print(si+5, sj-3)
                        #     check = True
                        #     break
                        # else:
                            print(1)
                            print(si+1, sj+1)
                            check = True
                            break
        elif pan[i][j] == 2:
            # cnt_w += 1
            for k in range(4):
                cnt_w = 1
                si, sj = i, j
                while True:
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < 19 and 0 <= nj < 19 and pan[ni][nj] == 2:
                        cnt_w += 1
                        i, j = ni, nj
                    else:
                        i, j = si, sj
                        break
                if cnt_w == 5:
                    if pan[si - di[k]][sj - dj[k]] != 2:
                        # if k == 3:
                        #     print(2)
                        #     print(si + 5, sj - 3)
                        #     check = True
                        #     break
                        # else:
                            print(2)
                            print(si+1, sj+1)
                            check = True
                            break
        if check == True:
            break
    if check == True:
        break
if check == False:
    print(0)