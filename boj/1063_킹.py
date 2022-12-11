# 220926_boj_1063_킹_실버3

chess = [[0] * 8 for _ in range(8)]
row = {'8':0,'7':1,'6':2,'5':3,'4':4,'3':5,'2':6,'1':7}
column = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}
move = {'R':[0,1], 'L':[0,-1], 'B' : [1,0], 'T':[-1,0], 'RT':[-1,1], 'LT': [-1,-1], 'RB':[1,1], 'LB':[1, -1]}

K, S, N = input().split()
K = list(K)         # king ( ex) ['A','1'] / 열, 행 쪼개서 받기 위해 list로 형변환 )
S = list(S)         # 돌

# dict key-value를 활용해서 초기 king/돌 행,열 위치 저장
ki = row[K[1]]      # king 행
kj = column[K[0]]
si = row[S[1]]      # 돌 행
sj = column[S[0]]

for i in range(int(N)):
    for di, dj in [move[input()]]:
        ni, nj = ki+di, kj+dj
        if 0<=ni<8 and 0<=nj<8:                 # 킹이 움직였을때 인덱스가 범위 내에 있고
            if ni == si and nj == sj:           # 킹이 움직였을때 돌의 위치와 겹치면
                if 0<=si+di<8 and 0<=sj+dj<8:   # 돌이 이동했을때 인덱스가 범위 내에 있는지 확인 후 킹,돌 둘 다 이동
                    ki, kj = ni, nj
                    si, sj = si+di, sj+dj
            else:                               # 킹이 움직여도 돌과 위치 같지 않으면
                ki, kj = ni, nj                 # 킹만 이동

for k, v in row.items():                        # 딕셔너리 value로 key 값 가져오기
    if v == ki:                                 # king 행
        ki = k
        break

for k, v in row.items():
    if v == si:                                 # 돌 행
        si = k
        break

for k, v in column.items():
    if v == kj:                                 # king 열
        kj = k
        break

for k, v in column.items():
    if v == sj:                                 # 돌 열
        sj = k
        break

print(f'{kj}{ki}')
print(f'{sj}{si}')