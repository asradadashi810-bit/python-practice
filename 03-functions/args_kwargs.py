# *args and **kwargs

# * collects any number of inputs (as a tuple)
def hello(*names):
    print(names)

hello("amirali", "asra", "sisi")


def hello_each(*names):
    for name in names:
        print(f"hello {name}")

hello_each("amirali", "asra", "sisi")


# ** collects keyword inputs (as a dict)
def info(fname, lname, *args, **kwargs):
    print(fname)
    print(lname)
    print(args)
    print(kwargs)

info("amirali", "asra", "sisi", age=20, city="tabriz")
