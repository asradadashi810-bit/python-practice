# Random choice from a list of names

import random

names = input("enter names (separated by space): ")

L = names.split()
print(L)

# Three random choices (may repeat)
print(random.choice(L))
print(random.choice(L))
print(random.choice(L))

# Or three different names (at least three names must be entered):
# print(random.sample(L, k=3))
