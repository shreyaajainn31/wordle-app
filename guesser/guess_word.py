import json
import os
import random
import boto3
from boto3.dynamodb.conditions import Key, Attr
from guesser.get_random_word import get_random_word
from guesser.get_length_of_word import get_length_of_word
from guesser.set_secret_word import set_secret_word

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('words')


secret_word = get_random_word()

# User would input the guess 
# From the user side, the clicks on the button would decide 
# Number of tries so frontend would send that 
   
def guess_word(event, context):
    guess = event['guess']
    n = get_length_of_word()
    tries = int(event['tries'])
    MAX_TRIES = n + 1
    
    print("secret ", secret_word)
    
    if secret_word is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Invalid input. There is no word with length {n}.'})
        }
    
    guess = guess.lower()
    if len(guess) != n:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Invalid input. Length of word should be {n} characters'})
        }
    
    green_letters_index = []
    yellow_letters_index = []
    grey_letters = []
    
    # There are following cases
    
    # 1. Letters are not in secret_word
    # If yes color changes to grey
    for char in guess:
        if char not in secret_word:
            grey_letters.append(char)
    
    # 2. If there are correct letters at the correct position
    # If yes color changes to green
    for i,char in enumerate(guess):
        if char == secret_word[i] and i not in green_letters_index:
            green_letters_index.append(i)
   
    # 3. If there are correct letters at the incorrect position
    # If yes color changes to yellow
    for i, char in enumerate(guess):
        if char in secret_word and char != secret_word[i] and i not in yellow_letters_index and i not in green_letters_index:
            yellow_letters_index.append(i)
            
    green_letters = [guess[i] for i in green_letters_index]
    yellow_letters = [guess[i] for i in yellow_letters_index]
    
    result = {
        'green_letters': green_letters,
        'yellow_letters': yellow_letters,
        'grey_letters': grey_letters
    }
    
    # We have the correct word
    if len(green_letters_index) == n:
        result['message'] = 'Congratulations!!!! '
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    
    tries += 1
    
    if tries < MAX_TRIES:
        result['tries'] = tries
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
    
    # Max tries reached
    result['message'] = 'Max tries reached'
    return {
        'statusCode': 400,
        'body': json.dumps(result)
    }
