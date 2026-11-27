# Store scores in a dictionary

name = input("enter your name: ")
m = {
    "math": int(input("enter your math score: ")),
    "sport": int(input("enter your sport score: ")),
    "art": int(input("enter your art score: ")),
    "english": int(input("enter your english score: ")),
}

avg = (m["math"] + m["sport"] + m["art"] + m["english"]) / 4
print(name)
print(m)
print("avg =", avg)
