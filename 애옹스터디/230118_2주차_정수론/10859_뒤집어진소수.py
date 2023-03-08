# boj_10859_뒤집어진 소수_정수론

N = int(input())
S = list(str(N))
nums = {'0':'0', '1': '1', '2': '2', '5':'5', '6':'9', '8':'8', '9':'6'}

if '3' in S or '4' in S or '7' in S:
    print('no')
else:
    checkN = False
    cnt = 0
    for i in range(2, int(N**0.5)+1):
        if N%i == 0:
            cnt += 1
    if cnt == 0:
        checkN = True

    for i in range(len(S)):
        S[i] = nums[S[i]]

    S = int(''.join(S[::-1]))
    cnt = 0
    for i in range(2, int(S**0.5)+1):
        if S%i == 0:
            cnt += 1
    if S == 1 or cnt != 0 or checkN != True:
        print('no')
    elif checkN == True and cnt == 0:
        print('yes')