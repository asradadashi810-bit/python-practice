# Read a text file and print the letters alternately in upper and lower case

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

for i in range(len(text)):
    if i % 2 == 0:
        print(text[i].upper(), end="")
    else:
        print(text[i].lower(), end="")
print()
