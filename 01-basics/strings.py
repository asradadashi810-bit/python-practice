# Working with strings

x = "asra"
print(len(x))        # length of the string
print(x[0])          # first character
print(x[len(x) - 1])  # last character
print(x[1:3])        # slicing
print(x[0:])         # from the start to the end
print(x.upper())
print(x.lower())

# Count the letters of a name (ignoring spaces and repeated letters)
name = input("enter your fullname: ")
name = name.lower()            # treat upper and lower case the same
name = name.replace(" ", "")   # remove spaces
seen = []
for ch in name:
    if ch not in seen:         # each letter is printed only once
        print(f"your name has {name.count(ch)} {ch}")
        seen.append(ch)

# f-string: the variable inside {} is replaced by its value
n = 7
print(f"number: {n}")   # number: 7
print("number: (n)")    # without {} the text is printed as it is
