# 0411 수업 중 지난 과제 복습
n = int(input())
arr = [1, 3, 4]
dp = [-1 for i in range(1010)]
def recur(cur):
    if cur < 0:         # 잘못낸경우, ex. 2개 남아있는데 3개 낸 경우
        return True
    if cur == 0:
        return False

    # 메모이제이션
    # if dp[cur] != -1:
    #     return dp[cur]

    # ret = True
    cnt = 0
    for i in arr:
        # ret &= recur(recur - i)

        # if cur - i < 0:   # 잘못낸경우, ex. 2개 남아있는데 3개 낸 경우 위에서 처리 안해주면 아예못들어가게 하면 됨
        #    continue
        if not recur(recur - i):
            cnt += 1

    # return not ret
    if cnt == 0:        # 상대가 한번도 못이겼으면 내가 이긴다
        # dp[cur] = False # 메모이제이션
        return False
    else:               # 상대가 한번이라도 이겼으면 내가 진다
        # dp[cur] = True # 메모이제이션
        return True

    # return dp[cur] # 메모이제이션
if recur(n):
    print("SK")
else:
    print("")