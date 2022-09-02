# IM 추천문제 boj_2309_일곱난쟁이

arr = []
s_list = [0,0,0,0,0,0,0]
for i in range(9):
    arr.append(int(input()))

# arr.sort()
hi = True
while hi:
    for i in range(3):
        s_list[0] = arr[i]
        for j in range(i+1,4):
            s_list[1] = arr[j]
            for k in range(j+1,5):
                s_list[2] = arr[k]
                for q in range(k+1, 6):
                    s_list[3] = arr[q]
                    for p in range(q+1,7):
                        s_list[4] = arr[p]
                        for t in range(p+1, 8):
                            s_list[5] = arr[t]
                            for o in range(t+1, 9):
                                s_list[6] = arr[o]
                                if sum(s_list) == 100:
                                    s_list.sort()
                                    for _ in s_list:
                                        print(_)
                                    hi = False
                                # else:
                                #     s_list.pop()
                                # s_list.clear()

# print(s_list)
