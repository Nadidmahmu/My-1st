import random as r

print("Welcome to my game. This is a Snake, Water, and Grass game.\n1. Type 0 to move snake\n2. Type 1 to move water\n3. Type 2 to move grass\n4. Type 3 to exit the game")

option = [0, 1, 2]
w, l, d = 0, 0, 0

while True:
    n = int(input())
    if n == 3:
        print(f"\nWin: {w}\nLose: {l}\nDraw: {d}")
        break
    elif n not in option:
        print("Invalid input")
        continue
    
    computer = r.choice(option)
    if n == computer:
        d += 1
        print("Draw")
    elif (n == 0 and computer == 2) or (n == 1 and computer == 0) or (n == 2 and computer == 1):
        w += 1
        print("You win")
    else:
        l += 1
        print("You lose")

