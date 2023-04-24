import json
import os
import random
import boto3
from boto3.dynamodb.conditions import Key, Attr
from get_word_length import get_word_length
import uuid

def get_random_word(game_id):
    """
    First it would get the length of the word by calling the get_length function
    defined in the get_word_length.py file. 
    Then, it would scan the "words" table to see how many words are present
    there of length n
    it would create an array of those n letter words and at the end
    return the random word from that array
    
    """
    
    # Define the DynamoDB resource object
    dynamodb = boto3.resource('dynamodb')  
    n = get_word_length(game_id)
    
    # create a table resource object for the words table
    words_table = dynamodb.Table('words')

    # get the words array consisting of 'n' letter words
    response = words_table.query(
        IndexName='word_length_index',
        KeyConditionExpression=Key('word_length').eq(n),
        ProjectionExpression='word'
    )
    
    words = [item['word'] for item in response['Items']]

    if words:
        word = random.choice(words)
        random_id = str(uuid.uuid4())
        id = str(uuid.uuid4())
        table_name = "secretWordTable"
        # putting the value of secret word with the game_id in the secret_word_table
        # with the secret word 
        secret_word_table = dynamodb.Table(table_name)
        item = {
            "id":random_id,
            "game_id":game_id,
            "word":word
        }
        secret_word_table.put_item(Item=item)
        return random.choice(words)
    else:
        return None
