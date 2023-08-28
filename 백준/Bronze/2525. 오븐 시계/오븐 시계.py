a,b = map(int,input().split())
c = int(input())
#일단 b+c 다 합친 것을 다른 변수 m으로 설정
#m=0
#최종적인 시간도 변수 h로 설정
#h=0

if b+c<=59:
    b=b+c
    h=a

else:
    m= b+c
    b= m % 60 #분은 60으로 나누고 남은 나머지.
        # 시간은 분을 60으로 나눈 몫만큼 더해져야함
    h = m//60 + a
    if h>=24:
        h= h%24 


print(h,b)