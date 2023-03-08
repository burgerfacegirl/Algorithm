# boj_14232_보석도둑

N = int(input())
a = b = 0

for i in range(int(N**0.5)+1, 3, -1):
    if N%i == 0:
        a, b = i, N//i
        break

print(a, b)
