
A, B, C = map(int,input().split())

if A == B == C :
    ans = 10000 + A * 1000
elif (A == B and B != C):
    ans = 1000 + A * 100
elif (B == C and A != B):
    ans = 1000 + B * 100
elif (A == C and A != B):
    ans = 1000 + A * 100
else:
    ans = max(A, B, C) * 100

print(ans)