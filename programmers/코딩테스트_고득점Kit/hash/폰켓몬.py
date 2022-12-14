# 221214_폰켓몬_level 1

def solution(nums):
    n = len(nums)
    p = n/2
    pick = len(set(nums))
    answer = pick if p >= pick else p
    return answer