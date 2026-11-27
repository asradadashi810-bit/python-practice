# Print prime numbers and perfect numbers up to n

n = int(input("enter n: "))

print("primes:")
for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):   # checking up to the square root is enough
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")

print("\nperfect numbers:")
for num in range(2, n + 1):
    sum_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        print(num, end=" ")
print()
