# boj_2725_보이는 점의 개수

# C = int(input())
# N = int(input())
#
# cp = [(i, i) for i in range(N+1)]
#
#
def gcd(i, j):
    if j == 0:
        return i
    return gcd(j, i % j)

cp = [0 for _ in range(1001)]
cp[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i == j:
            continue

        if gcd(i, j) == 1:
            cnt += 2
    cp[i] = cp[i-1] + cnt


T = int(input())
for _ in range(T):
    N = int(input())

    print(cp[N])
