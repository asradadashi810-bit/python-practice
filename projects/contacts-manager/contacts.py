"""Contacts manager: a simple phone book saved in a text file."""

from datetime import datetime

FILE_NAME = "contacts.txt"


def load_contacts():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_contacts(lines):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")


def get_name(line):
    return line.split(":")[0].strip()


def add_contact():
    name = input("name: ").strip()
    phone = input("number: ").strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(f"{name}: {phone} | {now}\n")
    print("saved!")


def show_all():
    lines = load_contacts()
    if not lines:
        print("no contacts yet.")
        return
    lines.sort(key=lambda line: get_name(line).lower())
    print("\n--- contacts ---")
    for line in lines:
        print(line)


def search_contact():
    query = input("write what you look for: ").strip().lower()
    found = False
    for line in load_contacts():
        if query in line.lower():
            print("found!!", line)
            found = True
    if not found:
        print("not found!", query)


def remove_contact():
    name = input("name for remove: ").strip().lower()
    kept = []
    for line in load_contacts():
        if name in get_name(line).lower():
            print(f"removed!: {line}")
        else:
            kept.append(line)
    save_contacts(kept)


def edit_contact():
    name = input("enter name: ").strip().lower()
    new_phone = input("enter number: ").strip()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = load_contacts()
    edited = False
    for i, line in enumerate(lines):
        if name in get_name(line).lower():
            original_name = get_name(line)
            lines[i] = f"{original_name}: {new_phone} | {now}"
            print(f"edited: {original_name} -> {new_phone}")
            edited = True
    if edited:
        save_contacts(lines)
    else:
        print("not found!")


def main():
    while True:
        print("\n--- contacts ---")
        print("1.add")
        print("2.see all")
        print("3.search")
        print("4.remove")
        print("5.edit")
        print("6.exit")

        choice = input("choose: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            remove_contact()
        elif choice == "5":
            edit_contact()
        elif choice == "6":
            print("bye!")
            break
        else:
            print("just choose 1 to 6!")


if __name__ == "__main__":
    main()
