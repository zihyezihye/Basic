a,b,c=map(int,input())
d,e,f=map(int,input())

first=(a*100+b*10+c)*f
second=(a*100+b*10+c)*e
third=(a*100+b*10+c)*d
total = first + second*10 + third*100

print(first)
print(second)
print(third)

print(total)