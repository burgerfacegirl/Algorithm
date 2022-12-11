# 그릇


arr = list(map(str,input()))

s = 10
for i in range(1, len(arr[1:])+1):
    if arr[i] == arr[i-1]:
        s += 5
    elif arr[i] != arr[i-1]:
        s += 10   
print(s)
