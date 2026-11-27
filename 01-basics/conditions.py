# Conditions (if / elif / else)

x = int(input("Enter a number: "))

# Positive, negative or zero
if x == 0:
    print("zero")
elif x > 0:
    print("positive")
else:
    print("negative")

# Even or odd
if x % 2 == 0:
    print("even")
else:
    print("odd")

# Age groups
age = int(input("enter the age: "))

if age < 13:
    print("child")
elif age <= 19:
    print("teenager")
elif age <= 59:
    print("young")
else:
    print("old")
