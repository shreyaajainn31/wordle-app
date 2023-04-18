import json
import string

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
    
    guess = guess.lower()
    
    if len(guess) != n:
        print("Invalid input. Length of word should be ", n, " characters")
        
    while tries < MAX_TRIES:
        
        greenLettersIndex = []
        yellowLettersIndex = []
        greyLetters = []
        
        # There are following cases
        
        
        # 1. Letters are not in SECRET_WORD
        # If yes color changes to grey
        for char in guess:
            if char not in SECRET_WORD:
                greyLetters.append(char)
        
        # 2. If there are correct letters at the correct position
        # If yes color changes to green
        
        for i,char in enumerate(guess):
            if char == SECRET_WORD[i] and i not in greenLettersIndex:
                greenLettersIndex.append(i)
       
        # 3. If there are correct letters at the incorrect position
        # If yes color changes to yellow
        for i, char in enumerate(guess):
            if char in SECRET_WORD and char != SECRET_WORD[i] and i not in yellowLettersIndex and i not in greenLettersIndex:
                yellowLettersIndex.append(i)
                
        print("These are the green letter words:")
        for char_index in greenLettersIndex:
            print(guess[char_index])

        print("These are the yellow letter words:")
        for char_index in yellowLettersIndex:
            print(guess[char_index])

        print("These are the grey letter words:")
        for char in greyLetters:
            print(char)

        # We have the correct word
        if len(greenLettersIndex) == n:
            print("Congratulations!!!! ")
            return [],[],[]       
            
        tries += 1
        
        if tries < MAX_TRIES:
            guess = input("Enter your guess: ")
        
    return greenLettersIndex, yellowLettersIndex, greyLetters