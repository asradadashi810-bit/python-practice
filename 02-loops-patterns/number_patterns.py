# Number patterns

n = int(input("n: "))

print("Triangle: numbers 1 to i in each row")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nTriangle with a continuous counter")
counter = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(counter, end=" ")
        counter += 1
    print()
