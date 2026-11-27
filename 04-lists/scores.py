# Read scores and calculate the average

scores = []

for i in range(5):
    score = float(input(f"enter score {i + 1}: "))
    scores.append(score)

print("\nscores:")
for s in scores:
    print(s)

total = 0
count_above_15 = 0
for s in scores:
    total += s
    if s > 15:
        count_above_15 += 1

average = total / len(scores)

print(f"\nAverage score: {average:.2f}")   # .2f means two decimal places
print(f"Number of scores above 15: {count_above_15}")
