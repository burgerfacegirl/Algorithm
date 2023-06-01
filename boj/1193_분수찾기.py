# boj_1193_분수찾기

n = int(input())

def find(arr, k):
    min_d = 9999999
    i = (n+1)//2
    flag = True
    while flag:
        if arr[i] > k:
            i -= 1
            if abs(arr[i]-k) < min_d:
                min_d = abs(arr[i]-k)
                



first_nums = [0] * (n+1)
first_nums[1] = 1

b = 2
i = 2
while i < n+1:
    if i % 2 == 0:
        first_nums[i] = first_nums[i-1] + b
        b += 4
    else:
        first_nums[i] = first_nums[i-1] + 1
    i += 1

if n in first_nums:
    print(str(first_nums.index(n))+"/1")
