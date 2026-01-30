import random
#generating a random number from 1 to 100
num = random.randint(0,100)

#guess function to ask the user for input
def guess():
    global guessNum #allows guessNum to be used throughout the code
    guessNum = int(input("Guess a number: "))
    return guessNum

#comparator function to compare user's guess and num
def comparator(a,b):
    if a > b: #if user's guess is higher than num
        return 0
    elif a < b: #if user's guess is lower than num
        return 1
    else: #if user's guess is the same as num
        return -1

#remark function to let user know if their guess it too high/low
def remark(val):
    while True:
        guess()
        val = comparator(guessNum, num)
        if val == 0:
            print("You guessed higher!")
            continue
        if val == 1:
            print("You guessed lower!")
            continue
        elif val == -1:
            print("You got it!")
            break #user guessed the number, so the loop breaks

#starting value = 0
startVal = 0
remark(startVal) #calling remark function with starting value