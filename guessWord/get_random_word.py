import json
import os
import random
import boto3
from boto3.dynamodb.conditions import Key, Attr
from get_word_length import get_word_length
from get_secret_word import get_secret_word

def guess_word(event,context):
    """
    This function has event as its parameter
    
    Event parameter will help in retrieving the guess from the user
    and number of tries user has done so far.
    
    Guess: It would be a string of n letter word
    Tries: We would get it from the frontend side depending upon the number
    of clicks on the "Enter" button.
    
    """
    
    game_id = event['game_id']
    length_of_word = get_word_length(game_id)
    secret_word = get_secret_word(game_id)
    max_tries = length_of_word + 1
    
   
    
    guess = event['guess']
    tries = int(event['tries'])
    
    if secret_word is None:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Invalid input. There is no word with length {n}.'})
        }
    
    guess = guess.lower()
    if len(guess) != length_of_word:
        return {
            'statusCode': 400,
            'body': json.dumps({'message': f'Invalid input. Length of word should be {n} characters'})
        }
    
    """
    The array below represent the following:
    
    1. green_letters_index: These represent the indexes of the characters of
    the string "guess" which are positioned correctly, as well 
    as guessed correctly
    
    2. yellow_letters_index: These represent the indexes of the characters of
    the string "guess" which are positioned incorrectly but 
    guessed correctly
    
    3. grey_letters: These are the letters which are neither positioned correctly,
    nor guessed correctly. 
    
    """
    
    green_letters_index = []
    yellow_letters_index = []
    grey_letters = []
    
    
    # Handling the grey_letters case 
    
    for char in guess:
        if char not in secret_word:
            grey_letters.append(char)
    
    # Handling green_letters case
    for i,char in enumerate(guess):
        if char == secret_word[i] and i not in green_letters_index:
            green_letters_index.append(i)
   
    # Handling yellow_letters case 
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
    if len(green_letters_index) == length_of_word:
        result['message'] = 'Congratulations!!!! '
        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }
        
    tries += 1
    if tries > max_tries:
        # Max tries reached
        result['message'] = 'Max tries reached'
        return {
            'statusCode': 400,
            'body': json.dumps(result)
        }

    
    return {
        'body': json.dumps(result)
    }