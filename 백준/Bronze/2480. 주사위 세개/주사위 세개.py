a,b,c = map(int,input().split())

if a== b== c:
    print(10000+a*1000)
elif a==b and c!=a:
    print(1000+a*100)
elif a==c and b!=a:
    print(1000+a*100)
elif b==c and a!=b:
    print(1000+b*100)
elif a!=b!=c and a>b and a>c:
    print(a*100)
elif a!=b!=c and b>a and b>c:
    print(b*100)
elif a!=b!=c and c>a and c>b:
    print(c*100)