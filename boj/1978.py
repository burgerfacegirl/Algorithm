N = int(input())
num_list = list(map(int,input().split()))
decimal = []

# for num in num_list: #num이 소수 list에 들어있으면 반복 끝남
#     n = 2
#     while num not in decimal :
#         if num%n:
#             n += 1
#             if num == 1:
#                 break
#         else:
#             if num == n:
#                 decimal.append(num)
#             elif num%n == 0:
#                 break

# print(len(decimal))



for num in num_list:
    n = 2
    while True : 
        if num%n: # num이 n으로 나누어 떨어지지 않으면
            n += 1 #n을 +1해서 다시 나눠줌
            if num == 1: #계속 나누다가 num 이 1이 되면
                break # 반복문 빠져 나감
        else: # num이 n으로 나누어 떨어지는데(위에서 계속 n 더해서 나눠주다가 옴)
            if num == n: #처음으로 나누어 떨어지는 나누는 수 n이 자기 자신(num)과 같으면
                decimal.append(num) #소수 list에 넣어줌
                break #반복문 끝
            elif num%n == 0: # 자기 자신과 같지 않은데 나누어 떨어지면 소수가 아니니까
                break # 그냥 반복문 빠져 나감

print(len(decimal))
