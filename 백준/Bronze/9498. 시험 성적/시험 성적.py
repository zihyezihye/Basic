scores = int(input())

if 90 <= scores <= 100:
    print('A')
elif 80 <= scores < 90 :
    print('B')
elif 70 <= scores < 80 :
    print('C')
elif 60 <= scores < 70 :
    print('D')
elif scores < 60 :
    print('F')