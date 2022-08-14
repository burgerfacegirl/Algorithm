# 블랙잭

# 순열 만들기

N, M = map(int,input().split())
arr = list(map(int,input().split()))
set1 = set()

for i1 in range(1,len(arr)):
    for i2 in range(1, len(arr)):
        if i1 != i2:
            for i3 in range(1, len(arr)):
                if i1 != i3 and i2 != i3:
                    s = arr[i1] + arr[i2] + arr[i3]
                    if s <= M:
                        set1.add(s)
print(max(set1))