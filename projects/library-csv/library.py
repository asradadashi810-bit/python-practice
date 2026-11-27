"""Library manager: books stored in a CSV file (needs: pip install tabulate)."""

import csv
from tabulate import tabulate

def menu():
    x = input("""
    1.show all books
    2.search book
    3.books with low stock
    4.top 3 books by copies
    5.add book
    6.remove book
    7.edit book
    8.exit
""")
    try:
        return int(x)
    except ValueError:
        return 0

def show_all_books():
    with open("books.csv", mode="r", encoding="utf-8") as f:
        data = csv.reader(f)
        h = next(data)
        res = list(data)

    print(tabulate(res,headers=h,tablefmt="heavy_grid"))

def search_book():
    with open("books.csv", mode="r", encoding="utf-8") as f:
        data = csv.reader(f)
        h = next(data)
        res = list(data)

        title = input("enter title: ")
        author = input("enter author: ")
        info = []
        for book in res:
            if book[1] == title and book[2] == author:
                info.append(book)

        print(tabulate(info, headers=h, tablefmt="heavy_grid"))

def low_stock_books():
    with open("books.csv", mode="r", encoding="utf-8") as f:
        data = csv.reader(f)
        h = next(data)
        res = list(data)

        threshold = 3
        info = []
        for book in res:
            copies = int(book[5])
            if copies < threshold:
                info.append(book)

        print(tabulate(info, headers=h, tablefmt="heavy_grid"))

def top3():
    with open("books.csv", mode="r", encoding="utf-8") as f:
        data = csv.reader(f)
        h = next(data)
        res = list(data)

        for book in res:
            book[5] = int(book[5])

        res.sort(key=lambda x: x[5], reverse=True)
        print(tabulate(res[:3], headers=h, tablefmt="heavy_grid"))        

def get_book_info():
    title = input("enter title: ")
    author = input("enter author: ")
    genre = input("enter genre: ")
    year = input("enter year: ")
    copies_available = input("enter copies available: ")
    return title, author, genre, year, copies_available

def get_last_id():
    with open("books.csv", mode="r", encoding="utf-8") as f:
        data = csv.reader(f)
        h = next(data)
        info = list(data)

        return int(info[-1][0])

def add_book():
    idx = get_last_id() + 1
    L = (idx,) + get_book_info()
    with open("books.csv", mode="a", newline="", encoding="utf-8") as f:
        data = csv.writer(f)
        data.writerow(L)

def remove_book():
    search_book()
    idx = input("enter an ID: ")
    with open("books.csv", mode="r", encoding="utf-8") as f:
        data = csv.reader(f)
        h = next(data)
        info = list(data)
        res = []
        for book in info:
            if idx != book[0]:
                res.append(book)
        with open("books.csv", mode="w", newline="", encoding="utf-8") as f2:
            data2 = csv.writer(f2)
            data2.writerow(h)
            data2.writerows(res)

def edit_book():
    search_book()
    idx = input("enter an ID: ")
    with open("books.csv", mode="r", encoding="utf-8") as f:
        data = csv.reader(f)
        h = next(data)
        info = list(data)
        res = []
        for book in info:
            if idx != book[0]:
                res.append(book)
            else:
                newInfo = (idx,) + get_book_info()
                res.append(newInfo)

    with open("books.csv", mode="w", newline="", encoding="utf-8") as f2:
        data2 = csv.writer(f2)
        data2.writerow(h)
        data2.writerows(res)


def main():
    while True:
        x = menu()
        if x == 1:
            show_all_books()
        elif x == 2:
            search_book()
        elif x == 3:
            low_stock_books()
        elif x == 4:
            top3()
        elif x == 5:
            add_book()
        elif x == 6:
            remove_book()
        elif x == 7:
            edit_book()
        elif x == 8:
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
