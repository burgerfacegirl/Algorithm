# boj_18310_안테나

N = int(input())

homes = list(map(int, input().split()))
homes.sort()

if N%2:
    ant = homes[N//2]
else:
    ant = homes[N//2-1]

print(ant)


