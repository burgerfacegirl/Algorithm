hour,minute = map(int,input().split())
time = int(input())

hour += time//60
minute += time%60

if minute >= 60:
    hour = hour + 1
    minute = minute - 60
if hour >= 24 :
    hour = hour - 24


print(f'{hour} {minute}')
