#220919_boj_13116_30_수학_트리_최소공통조상_실버2

# 포화 이진 트리

def find(v):
    parents = []
    while v :          # 조상 번호가 존재할 동안
        parents.append(v)   # 리스트에 부모 정점 번호 append
        v = tree[v]         # v에 부모 번호 담아줌(조상 번호 다 담아야하니까)
    return parents


T = int(input())
tree = [[] for _ in range(2**10)]
tree[0] = 0

for c in range(1, 2**10):
    tree[c] = c//2          # 자식을 인덱스로 부모 정점 번호를 담아줌(자식이 1023까지니까 index 1024까지)

for tc in range(1, T+1):
    A, B = map(int,input().split())

    # find(A), find(B)는 각각 A와 B의 부모를 담은 리스트로 반환됨 (숫자 큰 부모부터)

    for i in find(A):
        if i in find(B):
            print(i*10)
            break

    # print(find(A))
    # print(find(B))

