def solution(n):
    ans = 1

    while n != 1:
        if n % 2:
            n -= 1
            ans += 1
        else:
            n = n // 2

    return ans

# 풀이 참고해서 풀었음