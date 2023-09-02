# 세 정수 입력
a, b, c = map(int, input().split())

# 최솟값과 최댓값 찾기
min_val = min(a, b, c)
max_val = max(a, b, c)

# 최솟값과 최댓값이 아닌 정수가 두 번째로 큰 정수
second_largest = a + b + c - min_val - max_val

# 결과 출력
print(second_largest)