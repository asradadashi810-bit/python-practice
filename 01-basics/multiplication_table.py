# Multiplication table

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, " ", end="")
    print()
    print("-" * 40)

# Multiplication table of one number, using an f-string
# f-string: puts variable values directly inside the text
n = int(input("enter number: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")
