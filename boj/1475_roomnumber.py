# 220904_boj_1475_roomnumber
# import sys
numbers = list(map(int,input()))
# setN = set(numbers)
# cnt = 0
count = [0] * 10        # 각 숫자 개수 세어줄 카운트 배열

for i in numbers:
    count[i] += 1

maxV = 0
for j in range(len(count)):
    if maxV < count[j] and j != 6 and j != 9:   # 6, 9가 아닌 숫자 개수 중 최댓값(maxV)을 구함
        maxV = count[j]

# ex. 122266666 같은 거 때문에 6과 9를 포함해서 그냥 최댓값을 구해주면 안됨.

ans = 0
if (count[6]+count[9]) > maxV:              # 6 개수 + 9 개수가 maxV보다 크고
    if (count[6]+count[9]) % 2 == 0:        # 6 개수 + 9 개수가 짝수일때,
        if (count[6]+count[9])//2 > maxV:   # (6 개수 + 9 개수)//2가 maxV보다 크면
            ans = (count[6] + count[9])//2  # 해당 값으로 maxV값 갱신
        else:                               # (6 개수 + 9 개수)//2가 maxV보다 크지 않다면
            ans = maxV                      # ans는 그냥 maxV
    else:
        if ((count[6] + count[9])//2 + 1) > maxV:   # 위랑 같은데 6 개수 + 9 개수가 홀수일때
            ans = (count[6] + count[9])//2 + 1
        else:
            ans = maxV
else:
    ans = maxV                              # 6 개수 + 9 개수가 maxV보다 크지 않다면 ans는 그냥 maxV

print(ans)
# for i in setN:
#     if i == 9 or i == 6:
#         if (numbers.count(6) + numbers.count(9)) % 2:
#             cnt += (numbers.count(6) + numbers.count(9)) // 2 + 1
#             while 6 in numbers:
#                 numbers.remove(6)
#             while 9 in numbers:
#                 numbers.remove(9)
#         else:
#             cnt += (numbers.count(6) + numbers.count(9)) // 2
#             while 6 in numbers:
#                 numbers.remove(6)
#             while 9 in numbers:
#                 numbers.remove(9)
#     else:
#         if numbers.count(i) > 1:
#             cnt += numbers.count(i)
#         else:
#             cnt = 1
            # while i in numbers:
            #     numbers.remove(i)

# print(cnt)