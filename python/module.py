# import platform
# a = platform.system()
# print(a)

# import datetime

# b = datetime.datetime.now()
# print(b)

# import math
# c = math.sqrt(int(input()))
# print(c)

# import twomodules
# twomodules.name("aditya")

# import time
# v = time.localtime()
# print(v)


    


# import pygame

# pygame.mixer_music.play("aditya")
# pygame.mixer_music.load("aditya")


import random
print("Welcomr to sps game")
n = 10
number_of_die = 1
while(n >= 10):
    b = str(input("Enter your character:\n"))

    lis = ["stone","paper","scissors"]
    a = random.choice(lis)
    print(a)
    if (b == "paper"):
        if(a == "stone"):
            print("You win the match")
            

        elif(a == "paper"):
            print("This match is tie")
            
        elif(a == "scissors"):
            print("Yo losse the match")
            

    elif (b == "stone"):
        if (a == "stone"):
            print("This match is tie")
            
        elif(a == "paper"):
            print("You losse the match")
            
        elif(a == "scissors"):
            print("You win the match")
            

    elif (b == "scissors"):
        if (a == "stone"):
            print("You losse the match")
            
        elif(a == "paper"):
            print("ou win the match")
            
        elif(a == "scissors"):
            print("This match iis tie")

    else: 
        print(9-number_of_die,"no. of guesses left")
    number_of_die = number_of_die + 1

if (n == 10):
    print("Game over")




        
        

        