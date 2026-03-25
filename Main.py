import random

x = input("Press Enter To Play")

while x != "":
    x = input("Press Enter To Play")

print("Game Modes: \nEasy\nModerate\nDifficult")
# Easy - 10 questions all mutliple choice
# Medium - 10 multiple choice, 5 non-multiple choice
# Difficult - 20 non-multiple choice questions

gameMode = input("Enter the Game Mode You Want To Play: ")

 #if gameMode.casefold() == 