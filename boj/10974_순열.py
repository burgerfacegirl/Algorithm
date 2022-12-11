# 221006_boj_10974_순열_실버3

def permutation(i, k):
    if i == k:                          # k번째까지 숫자 정했으면
        print(*p)                       # 복사한 순열 출력
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = num[j]
                permutation(i+1, k)               # 다음 자리 적으러 이동
                used[j] = 0


N = int(input())
num = [i for i in range(1,N+1)]
used = [0] * (N+1)
p = [0] * N

permutation(0, N)

# 사전식 출력이 아님
# def permutation(i, k):
#     if i == k:
#         print(*num)
#     else:
#         for j in range(i, k):
#             num[i], num[j] = num[j], num[i]
#             permutation(i+1, k)
#             num[i], num[j] = num[j], num[i]
#
# N = int(input())
# num = [i for i in range(1,N+1)]
# permutation(0, N)
