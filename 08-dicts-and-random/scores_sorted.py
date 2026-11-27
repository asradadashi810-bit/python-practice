# Read four scores for two students, sort them and calculate the average


def read_student():
    name = input("enter your name: ")
    scores = [
        int(input("enter your math score: ")),
        int(input("enter your english score: ")),
        int(input("enter your art score: ")),
        int(input("enter your sport score: ")),
    ]
    scores.sort()
    avg = round(sum(scores) / len(scores), 2)
    print(name)
    print(scores)
    print("average:", avg)


read_student()
read_student()
