

# n=int(input("enter your number"))
# a=input("enter true or false")
# if (a=="true"):
#   for i in range(n):
#      print("*"*(i+1))
# elif (a=="false"):
#   for b in range(n):
#      print("*"*(n-b))
# else:
#   print("enter valid choice")




ad = int(input("Enter the number to how to print a *:\n"))
tf = int(input("Choice 1 for true or 2 for false:\n"))
if (tf == "1"):
  for i in range (ad):
    print("*"*(i+1))
elif (ad == "2"):
  for b in range (ad):
    print("*"*(ad-b))

# else:
#   print("invilde number")