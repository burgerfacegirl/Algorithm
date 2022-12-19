# 221216_위장_level 2
from itertools import combinations

def solution(clothes):
    clothes_cnt = {}
    answer = 0
    for clothe in clothes:
        if clothe[1] in clothes_cnt.keys():
            clothes_cnt[clothe[1]] += 1
        else:
            clothes_cnt[clothe[1]] = 1

    n = len(clothes_cnt)
    clothes_count = list(clothes_cnt.values())

    if n == 1:
        return clothes_count[0]
    else:   # 2개부터 조합 세주기
        answer += sum(clothes_count)  # 1개 입을 때 경우의 수
        # k = 2
        # while k <= n:
        #     for i in range(n-k):
        #         for j in range(i+1, i+k):
        #             answer += clothes_count[i] * clothes_count[j]
        #         k += 1
        k = 2
        while k <= n:
            a = 1
            clothes_comb = list(combinations(clothes_count, k))
            for i in clothes_comb:

            print(clothes_comb)
            k += 1

    return answer

print(solution([["a", "headgear"], ["b", "headgear"], ["c", "eyewear"], ["d", "eyewear"], ["e", "face"], ["f", "face"]]))