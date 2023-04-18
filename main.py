from guesser.guess_word import guess_word

print("this is your new guess game")
guess = input("Enter your guess: ")
n = int(input("Enter the length of the word: "))

guess_word(guess,n)