# 221024_greedy_01_모험가 길드_난이도 1

N = int(input())
people = list(map(int,input().split()))

people.sort()               # 오름차순 정렬 (최대 그룹수 세야하니까)

count = 0                   # 현재 그룹의 인원수
result = 0                  # 모험가 그룹
for i in people:
    count += 1              # 현재 그룹의 인원수 +
    if count >= i:          # 현재 그룹의 인원수가 현재 사람의 공포도보다 크거나 같으면
        result += 1         # 그룹 결성
        count = 0           # 현재 그룹 인원수 0으로 초기화하고 다음 그룹 확인
print(result)

# n = len(people)
# traveler = 0
# i = 0
# while True:
#     i += people[i]        # 공포도만큼 인덱스 더해줌
#     if i > N-1:           # 인덱스가 배열 벗어나면 반복문 종료
#         break
#     else:                 # 배열 벗어나지 않는다면 그룹 결성
#         traveler += 1
#
# print(traveler)
# 이 코드 반례 1 2 3 5 5      # 뒷 사람 공포도도 고려해줘야 하는데 고려 안 해줌 현재 사람 공포도만 고려해서 그룹 결성해서 틀림

