def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for test_num in [2, 3, 4, 5, 10, 13, 17]:
    print(f"{test_num} is prime? {is_prime(test_num)}")