# 221010_boj_2407_조합
# nCm을 출력한다.
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

n, m = map(int,input().split())

print((factorial(n)//(factorial(m)*factorial(n-m))))
