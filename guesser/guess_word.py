import json

API_URL = "/wordle/guess_word"
SECRET_WORD = ""


def guess_word(guess, n):
    global SECRET_WORD
    
    tries = 0
    MAX_TRIES = n+1
    
    if n == 5:
        SECRET_WORD = "apple"
    elif n == 6:
        SECRET_WORD = "letter"
    elif n == 7:
        SECRET_WORD = "eardrop"
    
    if len(guess) != n:
        print("Invalid input. Length of word should be ", n, " characters")
        return
        
    greenLettersIndex = []
    yellowLettersIndex = []
        
    while tries < MAX_TRIES:
        # Check if guess is total equal to the secret word
        if guess == SECRET_WORD:
            print("Correct word!")
            return
        
        # Otherwise there are two things we need to take care about
        
        # 1. If there are correct letters at the correct position
        # If yes color changes to green
        for i in range(len(guess)):
            char = guess[i]
            if char in SECRET_WORD and SECRET_WORD.index(char) == i and i not in greenLettersIndex:
                greenLettersIndex.append(i)
                    
        # 2. If there are correct letters at the incorrect position
        # If yes color changes to yellow
        for i in range(len(guess)):
            char = guess[i]
            if char in SECRET_WORD and SECRET_WORD.index(char) != i and i not in yellowLettersIndex and i not in greenLettersIndex:
                yellowLettersIndex.append(i)
        
        for index in greenLettersIndex:
            print("You have guessed ", guess[index], " correctly and at correct position")
        
        for index in yellowLettersIndex:
            print("You have guessed ", guess[index], " correctly but at wrong position")
        
        tries += 1
        
        if tries < MAX_TRIES:
            guess = input("Enter your guess: ")
        
    
    print("No correct guesses yet")
