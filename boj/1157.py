word = input().upper()
cnt_dict = {}
word_set = set(word)
word_count=[]

for i in word_set:
    cntW = 0
    for j in word:
        if i == j:
            cntW += 1
    cnt_dict[i] = cntW
    word_count.append(cntW)

maxV = max(cnt_dict.values())
r_cnt_dict = {v:k for k,v in cnt_dict.items()} # dict의 key, value 뒤집기

cnt = 0
for i in word_count:
    if maxV == i:
        cnt += 1
if cnt > 1:
    ans = '?'
else:
    ans = r_cnt_dict.get(maxV)

print(ans)

# for alphabet in cnt_list:
#     cnt=0
#     cnt += word.count(alphabet)
#     word_count.append(alphabet)
#     word_count.append(cnt)

# print(word_count)

# for i in range(1,len(cnt_list),2):
#     if cnt_list[i] >= cnt_list[i-2]:
#         cnt_max.append(cnt_list[i-1])

# print(cnt_max)
# if len(cnt_max) > 1:
#     print('?')
# elif len(cnt_max)==1:
#     print(cnt_max[0].upper())



    