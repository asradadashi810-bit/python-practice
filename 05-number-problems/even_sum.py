# Sum of even numbers from 1 to n

n = int(input("enter number: "))

sum_even = 0
i = 1
while i <= n:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"sum of even numbers up to {n}: {sum_even}")
