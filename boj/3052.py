# 나머지

arr = list(int(input()) for _ in range(10))
rest = []
for i in arr:
    rest.append(i%42)

print(len(set(rest)))