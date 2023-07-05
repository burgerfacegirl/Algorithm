def solution(s):
    alphas = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
              'eight': '8', 'nine': '9'}
    answer = ""

    n = len(s)
    start = 0
    end = 0

    while start < n and end < n:
        if s[start].isalpha():
            end += 3
            while True:
                if s[start:end] in alphas.keys():
                    answer += alphas[s[start:end]]
                    start = end
                    break
                else:
                    end += 1
        else:
            answer += s[start]
            start += 1
            end += 1

    return int(answer)