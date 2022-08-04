
a= int(input())
b= int(input())

third = a * (b%10)
fourth = (a * ((b%100)//10)) 
fifth = (a * (b//100))
ans = third + fourth*10 + fifth*100

print(third)
print(fourth)
print(fifth)
print(ans)