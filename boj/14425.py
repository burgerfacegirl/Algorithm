# 문자열 집합

# 힌트 덕분에 list-> set으로 고쳐서 겨우 맞긴 했지만 왜인지는 잘 모르겠다..
# 찾아보니까 중복되지 않는 값을 저장하고 확인할때는 list보다 set의 시간복잡도가 훨씬 작다고 한다.
# x in s 연산이 list 일때는 O(n), set 일때는 O(1)

N, M = map(int,input().split())

S = set()
words = []
for i in range(N):
    S.add(input())

for j in range(M):
    words.append(input())

cnt = 0
for i in range(len(words)):
    if words[i] in S:
        cnt+=1
print(cnt)
