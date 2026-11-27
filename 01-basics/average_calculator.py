# Read a name and four scores, then calculate the average

fname = input("First name: ")
lname = input("Last name: ")

score1 = float(input("Score of course 1: "))
score2 = float(input("Score of course 2: "))
score3 = float(input("Score of course 3: "))
score4 = float(input("Score of course 4: "))

average = (score1 + score2 + score3 + score4) / 4

print("Full name:", fname, lname)
print("Average:", average)
