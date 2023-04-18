from guesser.guess_word import guess_word

print("This is your new guess game")
guess = input("Enter your guess: ")
n = int(input("Enter the length of the word: "))

g, y, grey = guess_word(guess, n)

