# 221102_이코테 구현_boj_17413_단어뒤집기2_실버3

words = input()

if '<' not in words:        # 태그가 없는 순수 문자열
    strs = words.split()
    for str in strs:        # 그냥 각 문자열 뒤집고 그 사이에 공백 출력해줌
        str = str[::-1]
        print(str, end=' ')
else:                       # 태그가 있다면
    start = 0
    i = 0
    words = list(words)
    while i < len(words):
        if words[i] == '<':                                                  # 태그의 시작과 끝 체크해서 i 바꿔줌
            i += 1
            while words[i] != '>':
                i += 1
            i += 1
        elif words[i] != '<' and words[i] != '>' and words[i] != ' ':        # 문자열 일때
            start = i
            while i < len(words) and words[i] != '<' and words[i] != ' ' :   # 맨 앞에서 i 범위 검사 먼저 해줘야 함, 안 그러면 인덱스 에러 뜸
                i += 1
            words[start:i] = words[start:i][::-1]
        else:                                           # 공백일 때
            i += 1
    for i in words:
        print(i, end='')

# 문자열 일때 다음에 '<', 공백, 마지막 인덱스 3가지 체크해줘야함.
# 뒤집어야 하는 경우가 아래 3가지니까
# 1. >문자열<
# 2. >문자열(공백)
# 3. >문자열 => 문자 끝