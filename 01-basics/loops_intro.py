# Introduction to loops: while and for

# while
i = 10
while i > 5:
    print("greater than 5")
    i = i - 1

# Repeat a name as many times as the user wants
name = input("Enter a name: ")
number = int(input("Number of repeats: "))
while number > 0:
    print(name)
    number = number - 1

# for
for a in range(8):
    print(a)

# Repeat with for, and check for an invalid number
name = input("Enter a name: ")
num = int(input("Enter a number: "))
if num <= 0:
    print("nothing to repeat")
else:
    for i in range(num):
        print(name)

# Counter with while
count = 0
while count < 5:
    print(count)
    count += 1

# Guessing game: keep asking until the guess is 7
guess = 0  # must be defined first, with any number
while guess != 7:
    guess = int(input("Guess the number: "))
print("Well done!")
