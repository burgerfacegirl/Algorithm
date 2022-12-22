# 221221_2차원으로 만들기

# def solution(num_list, n):
#     answer = [[] for _ in range(len(num_list)//n)]
#     for i in range(len(num_list)):
#         answer[i//n].append(num_list[i])
#
#     return answer

def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        print(num_list[i:i+n])
        answer.append(num_list[i:i+n])
    return answer

print(solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3))