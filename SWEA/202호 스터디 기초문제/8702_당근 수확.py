
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    s = 0
    for i in arr:
        s += i
    s2 = 0
    cnt = 0
    for i in range(N):
        s2 += arr[i]
        if N % 2:
            if s2 == s//2:
                ans = i+1
                break
            if s2 > s//2:
                if sum(arr[0:i]) > sum(arr[i+1:N+1]):
                    ans = i
                    break
                else:
                    ans = i+1
                    break
        else:
            if s2 == s//2:
                ans = i+1
                break
            if s2 > s//2:
                if sum(arr[0:i]) < sum(arr[i+1:N+1]):
                    ans = i+1
                    break
                elif sum(arr[0:i]) >= sum(arr[i+1:N+1]):
                    ans = i
                    break

    person1 = sum(arr[0:ans])
    person2 = sum(arr[ans:N+1])
    print(f'#{tc} {ans} {max(person1,person2)-min(person1,person2)}')
