# 221212_level0_코딩테스트 입문_day2
# python의 math.gcd (최대 공약수 구하기) 혹은 분수 표시 및 분수 연산 모듈 fractions 활용

# 처음 내 풀이

from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    denum1 = denum1 * num2
    num = num1 * num2
    denum2 = denum2 * num1
    denum = denum1 + denum2

    bignum = denum if denum >= num else num

    for i in range(1, bignum + 1):
        if (denum % i == 0) and (num % i == 0):
            gcd = i

    answer = [denum // gcd, num // gcd]
    return answer

# fractions 활용 (fractions.Fraction)
# Fraction(a, b) 알아서 기약분수로 바꿔줌, 분모가 다른 두 분수 연산에 용이

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    answer = [answer.numerator, answer.denominator]
    return answer