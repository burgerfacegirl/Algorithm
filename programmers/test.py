def s(jobs):
    n = len(jobs)
    now = 0
    check = [0] * n
    c_i = [0] * 101
    did = []
    answer = []

    now_class = 0
    i = 1
    need = 0

    now += jobs[0][0] + jobs[0][1]
    did.append(jobs[0][2])
    now_class = jobs[0][2]
    check[0] = 1

    hey = []
    flag = True
    while sum(check) != n:
        # isItLonger = True
        flag = True
        if now < jobs[i][0]:
            now += jobs[i][1]
            if did[-1] != jobs[i][2]:
                did.append(jobs[i][2])
            check[i] = 1
            i += 1

        else:
            while i<n and jobs[i][0] <= now :
                if check[i] == 0:
                    hey.append(jobs[i]+[i])
                i += 1

            for job in hey:
                if job[2] == now_class:
                    now += job[1]
                    if did[-1] != job[2]:
                        did.append(job[2])
                    check[job[4]] = 1
                    hey.remove(job)
                    flag = False

            if flag:
                for job in hey:
                    c_i[job[2]] += job[3]

                most_info_class = c_i.index(max(c_i))
                now_class = most_info_class

                for job in hey:
                    if job[2] == now_class:
                        now += job[1]
                        if did[-1] != job[2]:
                            did.append(job[2])
                        check[job[4]] = 1
                        hey.remove(job)

            c_i = [0] * 101

    return did

# print(s([[1, 5,2,3], [2,2,3,2], [3,1,3,3], [5,2,1,5], [7,1,1,1], [9,1,1,1], [ 10,2,2,9]]))
print(s([[0,2,3,1], [5,3,3,1], [10,2,4,1]]))