# 최대공약수, 최소공배수

N,M = map(int,(input().split()))
N_list = []
M_list = []
A = N
B = M
i = 2
while N > 1:
    if N % i == 0:
        N_list.append(i)
        N = N//i
        if N % i:
            i += 1
    else:
        i += 1

k = 2
while M > 1:
    if M % k == 0:
        M_list.append(k)
        M = M//k
        if M % k:
            k += 1
    else:
        k += 1

gcd = 1

for i in N_list:
    if i in M_list:
        gcd = gcd * i
        M_list.remove(i)
        
print(gcd)        
print((A*B)//gcd)

print(max(N_list))