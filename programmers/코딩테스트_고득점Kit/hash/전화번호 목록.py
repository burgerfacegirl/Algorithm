# 221215_전화번호 목록_level2

def solution(phone_book):
    n = len(phone_book)
    answer = True
    phone_book.sort()
    for i in range(n):
        for j in range(i+1, n):
            if phone_book[i] not in phone_book[j]:
                break
            elif str(phone_book[i]) == str(phone_book[j])[0:len(str(phone_book[i]))]:
                answer = False
                break
        if answer == False:
            break

    return answer



# 다른 사람 풀이 (hash 이용)
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
print(solution(["119", "97674223", "1195524421"]))

# 다른 사람 풀이(zip 이용)

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True