# 221219_개미군단

def solution(hp):
    if hp%5==0:
        answer = hp//5
    elif (hp%5)%3 == 0:
        answer = hp//5+(hp%5)//3
    else:
        answer = hp//5+(hp%5)//3+(hp%5)%3
    return answer