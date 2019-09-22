#Lauren Gatesman
#Assignment 3, Problem 2
#Due September 26, 2019
#Class Section: 009
#ADD COMMENTARY BEFORE SUBMITTING

#Print out that introductory sentence and store secretnumber

print("I'm thinking of a number between 1 and 10!")

import random

secretnumber = int(random.randint(1,10))

#Ask user for their 3 guesses and print out corresponding responses, depending
#on if their guess is correct, too low, too high, or they ran out of guesses
                   
guess1 = int(input("What's your guess? "))

if guess1 == secretnumber :
    print("You got it!")
    print("The secret number was " + str(secretnumber) +".")
    print("It took you 1 try to guess the number.")
    

else:
    if guess1 > secretnumber :
        print("Too high, try again.")
        guess2 = int(input("What's your guess? "))
             
        if guess2 == secretnumber :
                print("You got it!")
                print("The secret number was " + str(secretnumber) +".")
                print("It took you 2 tries to guess the number.")

        else:
            if guess2 > secretnumber :
                print("Too high, try again.")
                guess3 = int(input("What's your last guess? "))
                
                if guess3 == secretnumber :
                    print("You got it!")
                    print("The secret number was " + str(secretnumber) +".")
                    print("It took you 3 tries to guess the number.")
             
                else:
                    print("The secret number was " + str(secretnumber) + ".")
                    print("You didn't guess the secret number.")
                    #END
            if guess2 < secretnumber :
                print("Too low, try again.")
                guess3 = int(input("What's your last guess? "))

                if guess3 == secretnumber :
                    print("You got it!")
                    print("The secret number was " + str(secretnumber) +".")
                    print("It took you 3 tries to guess the number.")
             
                else:
                    print("The secret number was " + str(secretnumber) + ".")
                    print("You didn't guess the secret number.")
                    #END
    if guess1 < secretnumber :
        print("Too low, try again.")
        guess2 = int(input("What's your guess? "))
             
        if guess2 == secretnumber :
            print("You got it!")
            print("The secret number was " + str(secretnumber) +".")
            print("It took you 2 tries to guess the number.")

        else:
            if guess2 > secretnumber :
                print("Too high, try again.")
                guess3 = int(input("What's your last guess? "))

                if guess3 == secretnumber :
                    print("You got it!")
                    print("The secret number was " + str(secretnumber) +".")
                    print("It took you 3 tries to guess the number.")
             
                else:
                    print("The secret number was " + str(secretnumber) + ".")
                    print("You didn't guess the secret number.")
                    #END
            if guess2 < secretnumber :
                print("Too low, try again.")
                guess3 = int(input("What's your last guess? "))

                if guess3 == secretnumber :
                    print("You got it!")
                    print("The secret number was " + str(secretnumber) +".")
                    print("It took you 3 tries to guess the number.")
             
                else:
                    print("The secret number was " + str(secretnumber) + ".")
                    print("You didn't guess the secret number.")
                    #END


    
