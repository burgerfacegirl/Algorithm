# 221216_외계행성의 나이

def solution(age):
    alpha_age = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}
    answer = ''
    for num in str(age):
        answer += alpha_age[num]
    # return ''.join(conv[i] for i in str(age))
    return answer


