# 0411 지난 과제(탑다운 dp) 복습
arr = list(map(int, input().split()))

def recur(a, b):
    if a<0 or b<0:
        return True
    if a < arr[0] and b < arr[0]: # 내가 낼 수 있는게 없으니까 내가 진거
        return False

    cnt = 0
    for i in arr:
        if not recur(a-i, b):
            cnt += 1

        if not recur(a, b-i):
            cnt += 1

    if cnt == 0:
        return False
    else:
        return True