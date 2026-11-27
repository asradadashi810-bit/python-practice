"""Store manager: products stored in an XML file (needs: pip install tabulate)."""

from tabulate import tabulate
import xml.etree.ElementTree as ET

tree = ET.parse("store.xml")
root = tree.getroot()

def menu():
    x = input("""
    1.show_all
    2.search
    3.export_low_stock
    4.add
    5.remove
    6.edit
    7.exit
""")
    try:
        return int(x)
    except ValueError:
        return 0

def show_all():
    res = []
    for p in root.findall("product"):
        idx = p.attrib["id"]
        name = p.find("name").text
        price = p.find("price").text
        count = p.find("count").text

        res.append([idx, name, price, count])
    h = ["id", "name", "price", "count"]
    print(tabulate(res, headers=h, tablefmt="heavy_grid"))

def search():
    name_input = input("enter product name: ")
    res = []
    for p in root.findall("product"):
        idx = p.attrib["id"]
        name = p.find("name").text
        price = p.find("price").text
        count = p.find("count").text
        if name == name_input:
            res.append([idx, name, price, count])
    h = ["id", "name", "price", "count"]
    print(tabulate(res, headers=h, tablefmt="heavy_grid"))

def export_low_stock():
    res = []
    for p in root.findall("product"):
        name = p.find("name").text
        count = int(p.find("count").text)
        if count < 5:
            res.append([name, count])
    h = ["name", "count"]
    print(tabulate(res, headers=h, tablefmt="heavy_grid"))

def add():
    last = int(root[-1].attrib["id"]) + 1
    idx = str(last)
    name = input("enter product name: ")
    price = input("enter price: ")
    count = input("enter count: ")

    product = ET.Element("product")
    product.set("id", idx)

    n = ET.SubElement(product, "name")
    n.text = name

    pr = ET.SubElement(product, "price")
    pr.text = price

    c = ET.SubElement(product, "count")
    c.text = count

    root.append(product)
    ET.indent(tree, "\t")
    tree.write("store.xml", encoding="utf-8")

def remove():
    search()
    idx = input("enter an id: ")

    for p in root.findall("product"):
        if idx == p.attrib["id"]:
            root.remove(p)
    ET.indent(tree, "\t")
    tree.write("store.xml", encoding="utf-8")

def edit():
    search()
    idx = input("enter an id: ")
    name = input("enter product name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    for p in root.findall("product"):
        if idx == p.attrib["id"]:
            p.find("name").text = name
            p.find("price").text = price
            p.find("count").text = count

    ET.indent(tree, "\t")
    tree.write("store.xml", encoding="utf-8")


def main():
    while True:
        x = menu()
        if x == 1:
            show_all()
        elif x == 2:
            search()
        elif x == 3:
            export_low_stock()
        elif x == 4:
            add()
        elif x == 5:
            remove()
        elif x == 6:
            edit()
        elif x == 7:
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
