num = int(input())

n = 2

while True:
    if num==1:
        break
    elif num%n == 0:
        num = num/n
        print(n)
    else:
        n = n+1