# Print and calculate a series with alternating signs and powers

i = 1
s = 0

while i <= 10:
    if i == 1:
        print(i, "^-", i + 1, sep="", end="")
        s = s + i ** (-(i + 1))
    elif i % 2 == 0:
        print(" - ", i, "^", i + 1, sep="", end="")
        s = s - i ** (i + 1)
    else:
        print(" + ", i, "^-", i + 1, sep="", end="")
        s = s + i ** (-(i + 1))

    i += 1

print()
print("Sum =", s)