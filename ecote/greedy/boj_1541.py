# boj 1541_잃어버린 괄호_실버2

ex = input().split('-')

plus_nums = []
ans = 0


# '-' 기준으로 양쪽 묶음 다 더해서 한번에 빼줌
for j in ex:
    cnt = 0
    nums = j.split('+')
    for k in nums:
        cnt += int(k)
    plus_nums.append(cnt)

first_num = plus_nums[0]
for i in range(1, len(plus_nums)):
    first_num -= plus_nums[i]

print(first_num)


# new_ex = []
# cal_ex = []
# minus = 0                           # 앞에 minus 있는지 여부
# ope = 0
# ans = 0
#
# for i in range(len(ex)):
#     if ex[i] == '+' or ex[i] == '-':
#         new_ex.append(int(ex[ope:i]))
#         new_ex.append(ex[i])
#         ope = i+1
#     elif i == len(ex) - 1:
#         new_ex.append(int(ex[ope:i+1]))
#
# for i in range(len(new_ex)):
#
#     if new_ex[i] == '-' and minus == 0:
#         minus = 1
#         ans += sum(new_ex[0:i])





