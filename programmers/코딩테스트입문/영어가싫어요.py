def solution(numbers):
    strToNum = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    answer = ''
    while len(numbers) > 0:
        for key in strToNum.keys():
            if numbers[0] == key[0]:
                if numbers[1] == key[1]:
                    answer += strToNum[key]
                    numbers = numbers[len(key)::]
                    break


    return answer

print(solution("onetwothreefourfivesixseveneightnine"))