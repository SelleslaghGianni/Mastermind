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

# Give the player 10 attempts before the game stops.
for attempts in range(10):
    print("Welcome to mastermind!")
    print("You can choose between these colours: Red(1), Green(2), Blue(3), Orange(4), Purple(5), Pink(6), Yellow(7) and Brown(8).")
    print("To do so, you have to enter the number correlating with the color and then press enter, four times in a row.")

    attempt = []
    rightPlace = 0
    wrongPlace = 0
    # DEBUG: print(answer)

    #This 
    for i in range(4):
        attempt.append(input("Please enter your answer. Remember to use numbers!\n"))

        if (attempt[i] == "1"):
            attempt[i] = 'Red'
        elif (attempt[i] == "2"):
            attempt[i] = 'Green'
        elif (attempt[i] == "3"):
            attempt[i] = 'Blue'
        elif (attempt[i] == "4"):
            attempt[i] = 'Orange'
        elif (attempt[i] == "5"):
            attempt[i] = 'Purple'
        elif (attempt[i] == "6"):
            attempt[i] = 'Pink'
        elif (attempt[i] == "7"):
            attempt[i] = 'Yellow'
        elif (attempt[i] == "8"):
            attempt[i] = 'Brown'
        else:
            attempt[i] = 'Wrong'

        print("You chose the answer: " + attempt[i] +".")

    for j in range(4):
        if (attempt[j] == answer[j]):
            rightPlace = rightPlace + 1
            continue
        for k in range(4):
            if (attempt[k] == answer[j]):
                wrongPlace = wrongPlace + 1

    if rightPlace == 4:
        print("Hooray!!!!! You guessed the 4 colors in the correct place!")
        break
    else:
        print("Try again!")
        print("Exact correct guesses: " + str(rightPlace) + ".")
        print("Correct color but in the wrong spot: " + str(wrongPlace) + ".")
        continue
