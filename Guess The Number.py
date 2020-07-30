import random #Module allows a random number to be generated.

#Next 2 lines allow the user to decide on the range of numbers rather than hardcoding them.
start = int(input("Enter the start of the range"))
end = int(input("Enter the end of the range"))

randomNumber = random.randrange(start,end) #Generates a random number within the range of start and end.

guess = int(input("Guess the number between the range")) #User makes their first guess.

while guess != randomNumber: #Every time the user's guess is wrong (can go on until the user guesses very number within the range).
    if guess - randomNumber >0: #If the user's guess is too high.
        print("Your guess was too high, try again") #Inform them.
        guess = int(input("Guess the number between the range")) #Prompt them to guess again.
    elif guess - randomNumber <0: #If the user's guess is too low.
        print("Your guess was too low, try again") #Inform them/
        guess = int(input("Guess the number between the range")) #Prompt them to guess again.
else: #Otherwise if their guess was/is correct.
    print("You guessed the number !!") #Let them know they got it correct.

'''
Line 12 explanation/example:
guess = 10
randomNumber = 8
8-10 leads to -2 (negative) therefore 10 was too high.

Line 15 explanation/example:
guess = 6
randomNumber = 10
10-6 = 4 (positive) therefore 6 was too low.
'''