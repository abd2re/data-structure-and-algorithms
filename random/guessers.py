#make a guessing game with a number of guesses
import time
import random
import numpy as np
import pandas as pd

secret = random.randint(1, 100)

def guessgame():
    guesses = 0
    guess = 0
    while guess != secret:
        guess = int(input("Guess a number between 1 and 100: "))
        guesses += 1
        if guess > secret:
            print("Too high")
        elif guess < secret:
            print("Too low")
        else:
            print("You got it!")
    #print("You guessed",secret,', after', guesses, "times")
    return guesses

def wahabAIsolver():
    #print('secret answer: ',secret)
    guesses = 0
    guess = 50
    cap = 101
    floor = 0
    found = False
    while not found:
        modificators = [32,16,8,4,2,1]
        #print("wahab's AI: ",guess)
        guesses +=1
        if guess > secret:
            #print(guess, " is too high")
            cap = guess
            for i in modificators:
                if guess - i > floor:
                    guess -= i
                    break

        elif guess < secret:
            #print(guess, " is too low")
            floor = guess
            for i in modificators:
                if guess + i < cap:
                    guess += i
                    break
        else:
            #print("You got it!, it's", guess)
            found = True

        #time.sleep(2)
    #print("You guessed",secret,', after', guesses, "times")
    return guesses



def mahounaAisolver():
    #print('secret answer: ',secret)
    guesses = 0
    cap = 100
    speed = 0
    floor = 1
    Found = False
    while not Found:
        guess = (cap + floor) // 2
        #print("mahouna's AI: ",guess)
        guesses += 1
        if guess > secret:
            #print(guess, " is too high")
            cap = guess
            #print("Too high")
        elif guess < secret:
            #print(guess, " is too low")
            floor = guess
            #print("Too low")
        else:
            #print("You got it!, it's", guess)
            Found = True
        #time.sleep(2)
    #print("You guessed",secret,', after', guesses, "times")
    return guesses



a = False
if a == True:
    name = input("what's your name: ")
    a = guessgame()
    #print('=================================================')
    time.sleep(2)
    b = wahabAIsolver()
    #print('=================================================')
    time.sleep(2)
    c = mahounaAisolver()
    #print('=================================================')
    time.sleep(2)
    #print(f'''{name} (stupid human): {a} tries
    #Wahab AI (smart robot): {b} tries
    #Mahouna AI (smartest robot): {c} tries''')




mahouguesses = []
wahabguesses = []
listofnum = []
for i in range(1,100):
    secret = i
    listofnum.append(i)
    n = mahounaAisolver()
    n2 = wahabAIsolver()
    mahouguesses.append(n)
    wahabguesses.append(n2)

a = np.array(mahouguesses)
#print('average',np.average(a))
#print('maximum',np.max(a))


b = np.array(wahabguesses)
#print('average',np.average(b))
#print('maximum',np.max(b))


