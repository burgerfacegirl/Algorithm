# boj_2309_일곱 난쟁이

shorts = [int(input()) for i in range(9)]
seven_shorts = []

for i in range(9):
    for j in range(i+1, 9):
        for k in range(j+1, 9):
            for p in range(k+1, 9):
                for q in range(p+1, 9):
                    for w in range(1+1, 9):
                        for o in range(w+1, 9):
                            if shorts[i] + shorts[j] + shorts[k] + shorts[p] + shorts[q] + shorts[w] + shorts[o] == 100:
                                seven_shorts.append([shorts[i], shorts[j], shorts[k], shorts[p], shorts[q], shorts[w], shorts[o]])
                                break

for seven_short in seven_shorts:
    seven_short.sort()
    for i in seven_short:
        print(i)
    break