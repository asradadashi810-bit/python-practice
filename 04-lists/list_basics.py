# List basics

nums = []
nums.append(5)      # add to the end of the list
nums.append(10)
print(nums)

# Sum
numbers = [1, 13, 18, 100]
total = 0
for n in numbers:
    total += n
print("sum:", total)

# Count the numbers greater than 10
numbers = [2, 8, 15, 33, 87]
count = 0
for n in numbers:
    if n > 10:
        count += 1
print("count > 10:", count)

# Largest number (use < instead of > for the smallest)
numbers = [1, 2, 6, 18, 888]
mx = numbers[0]
for n in numbers:
    if n > mx:
        mx = n
print("max:", mx)

# Average (len counts the items of the list)
nums = [10, 20, 30]
total = 0
for n in nums:
    total += n
print("average:", total / len(nums))

# factorial
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("factorial:", fact)
