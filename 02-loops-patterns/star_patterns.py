# Star patterns with nested loops

n = 5

print("1) Rectangle")
for i in range(3):
    for j in range(10):
        print("*", end=" ")
    print()

print("\n2) Increasing triangle")
for i in range(1, n + 1):
    print("* " * i)

print("\n3) Decreasing triangle")
for i in range(n, 0, -1):
    print("*" * i)

print("\n4) Right-aligned decreasing triangle")
n = 4
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)

print("\n5) Right-aligned increasing triangle")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

print("\n6) Half diamond (increasing then decreasing)")
n = 3
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)

print("\n7) Right-aligned half diamond")
for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (i + 1))

print("\n8) Diamond")
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
