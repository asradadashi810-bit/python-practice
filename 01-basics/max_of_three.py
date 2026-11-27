# Find the largest of three numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Method 1: with conditions
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# Method 2: with the max function
print(max(a, b, c))
