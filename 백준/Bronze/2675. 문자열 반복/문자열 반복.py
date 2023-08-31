t=int(input())

for i in range(t):
    r,s=input().split() #나란히 입력 받고 공백으로 나누기
    r=int(r) # r은 정수 처리해주기

    for a in s:
        print(a*r, end='')

    print() #줄 바꿈