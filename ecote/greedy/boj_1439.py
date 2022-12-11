# boj_1439_이코테_p.313 문자열 뒤집기_실버 5

S = input()

zero = 0
one = 0
for i in range(len(S)):
    if S[i] == '0' :
        if i == len(S)-1 or S[i+1] == '1':
            zero += 1
    else:
        if i == len(S)-1 or S[i+1] == '0':
            one += 1

ans = min(zero,one)                             # 연속된 0의 개수, 1의 개수 중 작은 수 출력
print(ans)