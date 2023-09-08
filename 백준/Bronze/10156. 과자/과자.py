# 과자의 가격, 과자 개수, 가지고 있는 돈을 입력받습니다.
price, quantity, money = map(int, input().split())

# 필요한 총 비용을 계산합니다.
total_cost = price * quantity

# 남은 돈을 계산합니다.
change = money - total_cost

# 만약 돈이 부족하면 부족한 금액을 출력합니다.
if change < 0:
    print(-change)
# 돈이 충분하면 0을 출력합니다.
else:
    print(0)