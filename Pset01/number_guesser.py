# ----------------------------------------------------------------------
# This is the file number_guesser.py
#
# The intent is to give you practice writing a complete, interactive
# Python program.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#git 
# Generate a random number between 1 and 1000.
#
# Ask the user to guess the number. In your prompt, let the user know they
# can type 'bye' or 'exit' to quit the program.
#
# If their guess is not made up entirely of digits, print "Please enter a valid
# number" and ask them to guess again.
#
# If the guess is too high, print "Too high!" and continue asking.
#
# If the guess is too low, print "Too low!" and continue asking.
#
# If the guess is correct, print "Congratulations! You guessed the number!" along
# with the number of attempts it took to guess the number. Start over with a new
# random number. Make sure to zero out the number of attempts.
#
# Please note: There are likely to be a number of Python guessing games online,
# and most GenAI systems can probably write this for you. Don’t rely on them,
# as they rob you of a chance to practice your Python skills and they might not
# even be correct. Perhaps, worse, they might not follow the instructions
# exactly as given.
# ----------------------------------------------------------------------
print("Welcome to the number guessing game!")
import random
counter = 0
number = random.randint(1, 1000)
input_str = input("Guess a number between 1 and 1000 (or type 'bye' or 'exit' to quit): ")
while input_str.lower() != "bye" and input_str.lower() != "exit":
    counter += 1
    if not input_str.isdigit():
        print("Please input a number")
    elif int(input_str) == number:
        print("Congratulations! You guessed the number!")
        print("This is how many guesses it took you!",counter)
        number = random.randint(1,1000)
        counter = 0
    elif int(input_str) > number:
        print("Too high")
    elif int(input_str) < number:
        print("Too low")
    input_str = input("Guess a number between 1 and 1000 (or type 'bye' or 'exit' to quit): ")
        
print("Goodbye!")
exit()

