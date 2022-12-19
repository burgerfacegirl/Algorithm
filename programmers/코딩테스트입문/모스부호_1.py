# 221219_모스부호1

def solution(letter):
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
    }

    list_letter = letter.split(" ")

    answer = ''
    for lett in list_letter:
        answer += morse[lett]

    return answer

print(solution(".... . .-.. .-.. ---"))