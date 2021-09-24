import random
list = ["Snake", "Water", "Gun"]
choice = random.choice(list)

def won():
    if i == 1:
        print("You won the ", i, "st game")
    elif i == 2:
        print("You won the ", i, "nd game")
    elif i == 3:
        print("You won the ", i, "rd game")
    else:
        print("You won the ", i, "th game")
    return i+1

def loose():
    if i == 1:
        print("You loose the ", i, "st game")
    elif i == 2:
        print("You loose the ", i, "nd game")
    elif i == 3:
        print("You loose the ", i, "rd game")
    else:
        print("You loose the ", i, "th game")
    return i+1

def draw():
    if i == 1:
        print("You draw the ", i, "st game")
    elif i == 2:
        print("You draw the ", i, "nd game")
    elif i == 3:
        print("You draw the ", i, "rd game")
    else:
        print("You draw the ", i, "th game")
    return i+1

sum = 0
add = 0





print("Let's play a game whose name is: Snake Water Gun:\nYou have to play 9 times: ")

i = 1
while i<10:
    print("Press:\n s for snake\n w for water\n g for gun: ")
    a = input()
    if a=="s":
        if choice=="Snake":
            print("You draw the game with the computer")
            print(draw())
            a = 1
            i=i+1

        elif choice=="Water":
            print("You won the game as snake drank the water")
            print(won())
            a = 2
            i = i + 1
        else:
            print("You loose the game as snake has been killed by the gun")
            print(loose())
            a = 3
            i = i + 1
    elif a=="w":
        if choice == "Water":
            print("You draw the game with the computer")
            print(draw())
            a = 1
            i = i + 1
        elif choice == "Snake":
            print("You loose the game as snake drank the water")
            print(loose())
            a = 3
            i = i + 1
        else:
            print("You won the game as gun sank in the water")
            print(won())
            a = 2
            i = i + 1
    elif a=="g":
        if choice == "Gun":
            print("You draw the game with the computer")
            print(draw())
            a = 1
            i = i + 1
        elif choice == "Snake":
            print("You won the game as snake has been killed by the gun")
            print(won())
            a = 2
            i = i + 1
        else:
            print("You loose the game as gun sank in the water")
            print(loose())
            a = 3
            i = i + 1
    else:
        print("Enter right choice: ")
        continue
    if a==2:
        sum=sum+1
    elif a==3:
        add=add+1

if sum>add:
    print("You won the game by winning ",sum," times")
else:
    print("You loose the game by loosing ",add," times")
