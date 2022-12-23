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

    dict = sorted(dict.items(), key = lambda item : item[0], reverse = True)

    answer = []

    ### lambda를 활용한 list, dict 정렬 더 공부해야겠다, 정렬 기준인 key가 뭐가 되는지 정렬된 결과가 어떻게 나오는지 등
    for genre in dict:
        ranked_song = sorted(dict_cnt[genre[0]], key=lambda  x: (-x[0], x[1]))
        best_album = 0
        for song in ranked_song:
            answer.append(song[1])
            best_album += 1
            if best_album == 2:
                break
        if len(answer) == 4:
            break
    # dict_cnt = sorted(dict_cnt.values(), key = lambda x: (-x[0], x[1]))
        # genres_set[genre] = sorted(dict_cnt.values(), key = lambda  x: (-x[0], x[1]))
    # dict_cnt = sorted(dict_cnt.items(), key = lambda  x: (-x[0], x[1]))

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

