# Rock, paper, scissors: 5 rounds against the computer

import random

L = ["rock","paper","scissors"]


count = 0

while count < 5 :
    pc = random.choice(L)


    user = input("rock / paper / scissors ? ").lower()

    if pc==user:
        print("draw")
    elif pc=="rock" and user=="paper":
        print("user win")
    elif pc=="rock" and user=="scissors":
         print("pc win")
    elif pc=="paper" and user=="rock":
         print("pc win")
    elif pc=="paper" and user=="scissors":
         print("user win")
    elif pc=="scissors" and user=="rock":
         print("user win")
    elif pc=="scissors" and user=="paper":
         print("pc win")

    print("pc:",pc,"user:",user)

    count += 1
    