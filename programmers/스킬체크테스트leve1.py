# 문제 2. 네오와 프로도의 숫자놀이

hi = "5fourthree2one"
alpha_num = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

for key, value in alpha_num.items():
    if value in hi:
        hi = hi.replace(value, key)

print(hi)