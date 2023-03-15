# boj_12101_1,2,3더하기 2

n, k = map(int, input().split())
nums = [1, 2, 3]
arr = []
ans_list = []
def recur(num, s):      # num 현재까지 쌓은 숫자, s는 현재까지 쌓은 숫자의 합
    global arr
    if s > n:
        return
    elif s == n:
        ans_list.append(num)
        return
    for i in range(1, 4):
        recur(num + [i], s + i)

recur([], 0)

if len(ans_list) >= k:
    print("+".join(map(str,ans_list[k-1])))
else:
    print(-1)