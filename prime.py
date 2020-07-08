def is_prime(n: int):
    if n == 2 or n == 3:
        return True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


N = int(input("ENter a limit"))
prime_no = []
for i in range(2, N):
    if is_prime(i):
        prime_no.append(i)
print(prime_no)