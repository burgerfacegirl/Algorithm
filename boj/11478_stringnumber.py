# 220912_bog_11478_서로 다른 부분 문자열의 개수_실버3

S = input()
set_S = set()

for i in range(len(S)+1):
    for j in range(i , len(S)):
        set_S.add(S[i:j+1])

print(len(set_S))
