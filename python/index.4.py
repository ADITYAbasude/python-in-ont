n = 10
mind = 1
print("Your number")
while (mind <= 10):
    # print("")
    geuss = int(input())
    if (geuss < 10):
        print("number is lower:")
    elif (geuss > 10):
        print("number is greater:")
    else :
        print("you win.")
        break
    print(10-mind,"die is left")
    mind = mind + 1

if (mind >10):
    print("game over")    