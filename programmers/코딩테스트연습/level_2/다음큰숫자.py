def solution(n):
    answer = 0

    def find_binary_one(m):

        binary_num = ""
        while m:
            binary_num += str(m % 2)
            m = m // 2
            #     어차피 1의 개수는 같으니까 뒤집지 않아도 됨
            cnt_one = binary_num.count("1")
        return cnt_one

    n_one = find_binary_one(n)
    for j in range(n + 1, 2 ** 20 + 1):
        if find_binary_one(j) == n_one:
            answer = j
            break

    return answer