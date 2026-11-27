# Function basics

def hello():
    print("hello")

hello()


def hello_name(name):
    print("hello", name)

hello_name(input("Enter a name: "))


def zarb(a, b):
    x = a * b
    print(x)

zarb(3, 4)


def add(a, b):
    return a + b          # we need return to get an output

print(add(3, 5))


def is_even(n):
    return n % 2 == 0

print(is_even(8))


def check(n):
    if n % 2 == 0:
        return "Even"
    return "Odd"

print(check(7))


def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total          # indentation is very important in Python

print(sum_to_n(5))
