while True:
    A, B = map(int, input().split())  # 두 개의 양의 정수 A와 B를 입력받습니다.
    
    if A == 0 and B == 0:  # 입력이 둘 다 0이면 종료합니다.
        break
    
    if A > B:
        print("Yes")
    else:
        print("No")





