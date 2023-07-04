def solution(n, arr1, arr2):
    def make_binary(k):
        b = ""
        while k > 0:
            b += str(k % 2)
            k //= 2

        if len(b) < n:
            b = b + (n - len(b)) * "0"

        return b[::-1]

    arr_a = []
    arr_b = []

    for num in arr1:
        arr_a.append(make_binary(num))

    for num in arr2:
        arr_b.append(make_binary(num))

    answer = []

    for i in range(n):
        tmp = ""
        for j in range(n):
            if int(arr_a[i][j]) or int(arr_b[i][j]):
                tmp += "#"
            else:
                tmp += " "
        answer.append(tmp)

    return answer