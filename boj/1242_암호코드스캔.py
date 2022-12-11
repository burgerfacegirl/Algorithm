#220920_Start2_SWEA_1242_암호코드 스캔


preorder = []       # 전위 순회로 읽은 값 입력 받음
while True:
    try:
        preorder.append(int(input()))
    except:
        break
print(preorder)
