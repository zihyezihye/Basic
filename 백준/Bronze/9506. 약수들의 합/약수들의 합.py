def find_divisors_sum(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors

def main():
    while True:
        n = int(input())
        if n == -1:
            break

        divisors = find_divisors_sum(n)
        divisors_sum = sum(divisors)

        if divisors_sum == n:
            print(f"{n} =", " + ".join(map(str, divisors)))
        else :
            print(f"{n} is NOT perfect.")


if __name__ == "__main__":
    main()