# 평균 점수
arr = []

for i in range(5):
    arr.append(int(input()))

for j in range(5):
    if arr[j] < 40:
        arr[j] = 40
# for j in arr:
#     print(j)
#     if j < 40:
#         j = 40

print(sum(arr)//len(arr))

# 왜 index말고 그냥 j로 하면 안되지 ? 질문