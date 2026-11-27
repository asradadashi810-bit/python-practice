# Function exercises

# --- Password validation ---
def pass_validation(password):
    if len(password) < 8:
        print("your password must be at least 8 char")
        return False
    elif password.isnumeric():
        print("your password must have at least one letter")
        return False
    elif password.isalpha():
        print("your password must have at least one number")
        return False
    print("yes your password is correct!")
    return True


# --- Count upper and lower case letters ---
def count_cases(name):
    ups = 0
    lows = 0
    for n in name:
        if n.isupper():
            ups += 1
        elif n.islower():
            lows += 1
        else:
            pass  # do nothing and move on
    print(f"upper cases: {ups}")
    print(f"lower cases: {lows}")


# --- Convert a Persian (Solar Hijri) birth year to Gregorian (approximate) ---
def converter(day, month, year):
    if month > 10:
        birthday = year + 622
    elif day > 10 and month == 10:
        birthday = year + 622
    else:
        birthday = year + 621
    print(f"your year of birthday is {birthday}")


# --- Average and status ---
def grade_report(name, x, y, z):
    avg = (x + y + z) / 3
    if avg >= 17:
        status = "perfect!"
    elif avg >= 12:
        status = "good!"
    else:
        status = "try more!"
    print(f"{name}, {avg:.2f}, {status}")  # print must be inside the function


if __name__ == "__main__":
    # Password: keep asking until a valid one is entered
    while True:
        if pass_validation(input("enter your password: ")):
            break

    count_cases(input("enter your name: "))

    converter(int(input("enter day: ")),
              int(input("enter month: ")),
              int(input("enter year: ")))

    name = input("enter your name: ")
    g1 = float(input("enter grade 1: "))
    g2 = float(input("enter grade 2: "))
    g3 = float(input("enter grade 3: "))
    grade_report(name, g1, g2, g3)
