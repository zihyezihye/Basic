x= int(input())
n= int(input())

sum=0

for i in range(n):
    a,b = map(int,input().split())
    mul= a*b
    sum+=mul

if sum == x:
    print("Yes")
else :
    print("No")