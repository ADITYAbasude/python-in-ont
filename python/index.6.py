import datetime
print("Health manegment")
print("press 1 for aditya and press 2 for kiran")
def gettime():
    return datetime.datetime.now()
press = int(input())
if (press == 1):
    print("You are in Aditya:")
    print("press 3 for lock food and press 4 for lock yoga")
    a = int(input())
    if (a == 3):
        print("Type a letter to your grahak:")
        with open("aditya.txt", "w")as f:
            f.write(input())
            print(f.write)
            print("succesfully done")
            
    elif (a == 4):
        print("Type a letter to your grahak:")
        with open("aditya.txt", "w")as f:
            f.write(input())
            print(f.write)
            print("succesfully done")

elif (press==2):
    print("You are in kiran:")
    print("press 3 for lock food and press 4 for lock yoga")
    a = int(input())
    if (a == 3):
        print("Type a letter to your grahak:")
        with open("aditya.txt", "w")as f:
            f.write(input())
            print(f.write)
            print("succesfully done")
    elif (a == 4):
        print("Type a letter to your grahak:")
        with open ("aditya.txt","w") as f:
            f.writelines(input())
            print(f.write)
            print("succesfully done")

else:
    print("Enetr a valide number")
    