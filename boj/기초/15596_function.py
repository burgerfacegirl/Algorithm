#221916_boj_15596_정수N개의합_브론즈2

def solve(a):
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans