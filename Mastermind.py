import random

# 8 colors to pick 1 random, have to call this function 4 times. Got this from stackoverflow.
COLORS = ["Red", "Green", "Blue", "Orange", "Purple", "Pink", "Yellow", "Brown"]
# Getting lists and ints ready to use them later on.
answer = []

# Using the COLORS list I used a randomizer. This will return a random color.
def randomColor():
    return random.choice(COLORS)

# Looping the randomColor() function to append the result in the answer variable.
def pickColor():
    for i in range(4):
        # DEBUG: print(randomColor())
        answer.append(randomColor())

pickColor()
# DEBUG: print(answer)
print("Welcome to mastermind!")
print("To win this game you have to guess the randomly generated colors. Keep in mind that a color can be generated multiple times.")

# Give the player 10 attempts before the game stops.
for attempts in range(10):
    
    print("You can choose between these colours: Red(1), Green(2), Blue(3), Orange(4), Purple(5), Pink(6), Yellow(7) and Brown(8).")
    print("To do so, you have to enter the number correlating with the color and then press enter, four times in a row.")

    attempt = []
    rightPlace = 0
    wrongPlace = 0
    
    # This part of the code asks you to enter your answer and then turns the number into a word. It also tells the player what color he entered, sort of as a debugger.
    for i in range(4):
        attempt.append(input("Please enter your answer. Remember to use numbers!\n"))

        if attempt[i] == "1":
            attempt[i] = 'Red'
        elif attempt[i] == "2":
            attempt[i] = 'Green'
        elif attempt[i] == "3":
            attempt[i] = 'Blue'
        elif attempt[i] == "4":
            attempt[i] = 'Orange'
        elif attempt[i] == "5":
            attempt[i] = 'Purple'
        elif attempt[i] == "6":
            attempt[i] = 'Pink'
        elif attempt[i] == "7":
            attempt[i] = 'Yellow'
        elif attempt[i] == "8":
            attempt[i] = 'Brown'
        else:
            attempt[i] = 'Wrong'

        print("You chose the answer: " + attempt[i] +".")

    # This part checks if the answers are ok. It's a nested loop because I want to check for both exact correct numbers and correct numbers in the wrong slot.
    # After that it either ends the game or it tells the player to try again and some information.
    for j in range(4):
        if attempt[j] == answer[j]:
            rightPlace = rightPlace + 1
            continue
        for k in range(4):
            if attempt[k] == answer[j]:
                wrongPlace = wrongPlace + 1

    if rightPlace == 4:
        print("Hooray!!!!! You guessed the 4 colors in the correct place!")
        break
    else:
        print("Try again!")
        print("Exact correct guesses: " + str(rightPlace) + ".")
        print("Correct color but in the wrong spot: " + str(wrongPlace) + ".")
        continue