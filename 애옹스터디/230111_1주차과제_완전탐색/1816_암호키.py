# boj_1816_암호 키

def isItPrime(num) :
    primes = [1] * num
    print(primes)
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

N = int(input())

for _ in range(N):
    s = int(input())
    ans = 'Yes'

    for j in range(2, int(s**0.5)+1):
        if s%j == 0:
            if (isItPrime(j) != True) or (j <= 10**6) :
                ans = 'No'
                break

    print(ans)


