# 220915_boj_1991_트리순회_트리_재귀_실버1

def preorder(n):                # 전위 순회
    global pr_ans
    if n and n != '.':          # 정점이 존재하고 그 값이 '.'이 아니면 ('.'이면 비어있는 거)
        pr_ans += n            # 루트
        preorder(tree[n][0])    # 왼쪽 자식 ( tree['A'] = ['B', 'C'] )
        preorder(tree[n][1])    # 오른쪽 자식

def inorder(n):                 # 중위 순회
    global in_ans
    if n and n != '.':
        inorder(tree[n][0])     # 왼쪽 자식
        in_ans += n             # 루트
        inorder(tree[n][1])     # 오른쪽 자식

def postorder(n):               # 후위 순회
    global po_ans
    if n and n != '.':
        postorder(tree[n][0])   # 왼쪽 자식
        postorder(tree[n][1])   # 오른쪽 자식
        po_ans += n             # 루트

N = int(input())    # 노드(정점) 개수
tree = {}           # 딕셔너리, 노드가 알파벳으로 들어오니까 그걸 키 값으로

for i in range(1, N+1):
    n, c1, c2 = input().split()     # 루트 노드, 왼쪽 자식 값, 오른쪽 자식 값
    pr_ans = ''     # 전위 순회 답
    in_ans = ''     # 중위 순회 답
    po_ans = ''     # 후위 순회 답
    tree[n] = [c1, c2]

preorder('A')                       # 루트 노드 무조건 'A'니까 'A'부터 호출
inorder('A')
postorder('A')

print(pr_ans)
print(in_ans)
print(po_ans)
