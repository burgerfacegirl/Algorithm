word = input().lower()
cnt_dict = {}
word_set = set(word)
word_count=[]
for i in word:
    if i in cnt_dict:
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1

print(cnt_dict)
    # cnt_list.append(i)
    # cnt = 0
    # cnt += word.count(i)
    # cnt_list.append(i)
    # cnt_list.append(word.count(i))
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



    