N = int(input())
num_list = list(map(int,input().split()))
decimal = []

for num in num_list:
    n = 2
    while num not in decimal :
        if num%n:
            n += 1
            if num == 1:
                break
        else:
            if num == n:
                decimal.append(num)
            elif num%n == 0:
                break

print(len(decimal))