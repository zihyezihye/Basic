import math

def find_lcm(a, b):
    return (a * b) // math.gcd(a, b)

T = int(input())  # 테스트 케이스 수 입력

for _ in range(T):
    A, B = map(int, input().split())  # 두 개의 자연수 A와 B 입력
    result = find_lcm(A, B)  # 최소공배수 계산
    print(result)