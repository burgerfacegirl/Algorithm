# boj_9417_최대 GCD_정수론

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N = int(input())

for tc in range(N):
    nums = list(map(int,input().split()))
    ans = -100
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if ans <= gcd(nums[i], nums[j]):
                ans = gcd(nums[i], nums[j])
    print(ans)