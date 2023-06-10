def solution(n, words):
    cnt = [0] * (n)
    #     1번 사람부터 확인할 거니까 0번 차례는 1로 두고 시작
    cnt[0] = 1
    dropout = 0
    cnt_dropout = 0
    i = 1
    j = 1

    while dropout == 0 and i < len(words):
        if len(words[i]) == 1 or words[i][0] != words[i - 1][-1] or words[i] in words[0:i]:
            dropout = j + 1
            cnt_dropout = cnt[j] + 1
            break
        else:
            cnt[j] += 1
            i += 1
            j += 1
        if j == n:
            j = 0

    answer = [dropout, cnt_dropout]
    return answer

