# boj_1759_암호 만들기

# C 개 중 L개 중복 없이 뽑기 순열, 오름차순
L, C = map(int, input().split())
alphas = list(input().split())
alphas.sort()
arr = ['' for _ in range(L)]
consonant = 'aeiou'
vowel = 'bcdfghjklmnpqrstvwxyz'

def recur(cur, start):
    if cur == L:
        cnt_con = 0
        cnt_vow = 0
        for con in consonant:
            if con in arr:
                cnt_con += 1
        for vow in vowel:
            if vow in arr:
                cnt_vow += 1
        if cnt_con >= 1 and cnt_vow >= 2:
            print(''.join(arr))
            return
        return

        print(*arr)
        return
    for i in range(start, C):
        arr[cur] = alphas[i]
        recur(cur + 1, i + 1)

recur(0, 0)
