#220928_boj_6603_로또_실버2
def nCr(n, num, r):
    if n == len(S):
        if len(num) == r:
            tmp = [i for i in num]
            lottos.append(tmp)
        return
    num.append(S[n])
    nCr(n+1, num, r)
    num.pop()
    nCr(n+1, num, r)

while True:
    # if input() == '0':
    #     break
    # k, *S = map(int,input().split())
    N = list(map(int,input().split()))
    k = N[0]
    S = N[1:]
    if k == 0:
        break
    lottos = []
    nCr(0, [], 6)
    for i in lottos:
        for j in i:
            print(j, end=' ')
        print()
    print()

    # for i in range(k):
    #     for j in range(k):
    #         if i != j:
    #             for q in range(k):
    #                 if i != q and j != q:
    #                     for p in range(k):
    #                         if i != p and j!= p and q != p:
    #                             for h in range(k):
    #                                 if i != h and j != h and q != h and p != h:
    #                                     for x in range(k):
    #                                         if i != x and j != x and q != x and p != x and h != x:
    #                                             print(i, j, q, p, h, x)

