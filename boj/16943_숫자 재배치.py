#221010_boj_16943_숫자 재배치

def p(K):
    global maxV                             # 후보가 너무 많아서 일단 한 번 걸러주려고.. 근데 어차피 밑에서 한번 더 max 쓰니까 걸리는 시간 같나..?
    if K == len(N):
        s = ''.join(results)
        if s[0] != '0':                     # 첫째자리가 0이 아닐때
            if int(s) < B:                  # B보다 작으면 maxV랑 비교하고(후보 줄이려고) 리스트에 담아줌
                if maxV < int(s):
                    maxV = int(s)
                    result.append(int(s))
    else:
        for i in range(len(N)):
            if used[i] == 0:
                used[i] = 1
                results[K] = N[i]
                p(K+1)
                used[i] = 0



A, B = map(int,input().split())
N = []
result = []                                 # A로 만든 순열 중 B보다 작은 숫자 담을 리스트

while A>0:
    N.append(str(A%10))                     # 순열 만들어서 join 함수 써야돼서 str로 바꿔줌
    A //= 10                                # A 각 숫자 쪼개서 리스트 N에 담아줌 (순열 만들어야 하니까)

used = [0] * len(N)
results = [0] * len(N)                      # A로 만든 순열 담을 리스트
maxV = -10000

p(0)

if len(result) == 0:
    print(-1)
else:
    print(max(result))
