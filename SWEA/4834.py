# 1일차 - 숫자 카드(제출용)

import sys
sys.stdin = open('4834.txt')
# T = int(input())

# for tc in range(1,T+1):
#     N = int(input())
#     arr = list(map(int, input()))

#     # arr 의 원소에 대한 카운트 배열 만들기(숫자 카드 0~9 장수 세기)
#     cnt = [0]*10
#     for num in arr:
#         cnt[num] += 1

#     max_V = cnt[0]
#     max_index = 0
#     for i in range(len(cnt)):
#         if cnt[max_index] <= cnt[i]:
#             max_index = i
    
#     print(f'#{tc} {max_index} {cnt[max_index]}')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input()))
    count = [0] * 10
    for i in range(N):
        count[arr[i]] += 1
    
    maxI = 0
    for i in range(len(count)):
        if count[i] >= count[maxI]:
            maxI = i

    print(f'#{tc} {maxI} {count[maxI]}')
    # maxV = nums[0]
    # for i in range(N):
    #     if nums[i] > maxV :
    #         maxV = nums[i]
    
    # count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # for i in range(N):
    #     count[nums[i]] +=1

    # max_count = count[0]
    # max_index = 0
    # for i in range(len(count)):
    #     if count[i] >= max_count:
    #         max_index = i
    #         max_count = count[i]
    # print(f'#{tc} {max_index} {max_count}')
