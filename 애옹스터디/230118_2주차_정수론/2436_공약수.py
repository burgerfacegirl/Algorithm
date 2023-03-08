# boj_2436_공약수

from math import sqrt

min_sum = 200000000

g, l = map(int, input().split())

div = l // g  # a*b = l/g

# 유클리드 호제법
def gcd(a, b):
    if a % b == 0:
        return b  # 최대공약수

    return gcd(b, a % b)


for a in range(1, int(sqrt(div)) + 1):  # 1부터 divide의 제곱근까지 돌면서
    b = int(div / a)  # b = (l/g)/a

    if div % a == 0 and gcd(a, b) == 1:  # 약수고 서로소면
        if b - a < min_sum:  # 합이 최소면
            min_sum = b - a
            x = a*g
            y = b*g

print(x, y)