# 221222_베스트앨범_level3

def solution(genres, plays):
    dict = {}
    dict_cnt = {}
    genres_set = set(genres)
    for genre in genres_set:
        dict[genre] = 0
        dict_cnt[genre] = []
    for i in range(len(genres)):
        dict[genres[i]] += plays[i]
        dict_cnt[genres[i]].append([plays[i], i])
    print(dict_cnt)
    for item in dict_cnt.items():
        print(item)
    dict = sorted(dict.items(), key = lambda item : item[0], reverse = True)
    dict_cnt = sorted(dict_cnt.items(), key = lambda  x: (-x[0], x[1]))

    answer = []
    return dict, dict_cnt

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))