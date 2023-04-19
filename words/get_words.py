
import os

filename = os.path.join(os.getcwd(), 'words', 'nounlist.txt')

def fetch_words(n):
    with open(filename, 'r') as file:
        words = [line.strip() for line in file if len(line.strip()) == n]
    return words


five_letter = fetch_words(5)
six_letter = fetch_words(6)
seven_letter = fetch_words(7)
eight_letter = fetch_words(8)

print(seven_letter)
print(eight_letter)