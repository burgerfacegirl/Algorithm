#링

N = int(input())

r = list(map(int,input().split()))

cd_list = []
gcd = 1
def gcd_f(a,b):
    A = min(a,b)
    for i in range(1,A+1):
        if a%i == 0 and b%i ==0:
            cd_list.append(i)
            gcd = max(cd_list)
    return gcd

for i in range(len(r)-1):
    print(f'{r[0]//gcd_f(r[0],r[i+1])}/{r[i+1]//gcd_f(r[0],r[i+1])}')
    cd_list.clear() # clear 안해주면 cd_list 안 지워져서 앞에 거 그대로 저장됨.. 더 큰 수로 ex) 8 4 2 면 8 2 최대공약수 4로 나옴


    # if r[0]%r[i+1] == 0 :
    #     print(f'{r[0]//r[i+1]}/1')
    # else :
    #     print(f'{r[0]//gcd_f(r[0],r[i+1])}/{r[i+1]//gcd_f(r[0],r[i+1])}')
       