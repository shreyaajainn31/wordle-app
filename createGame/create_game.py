import json
import os
import random
import uuid
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table_name = 'userEntry'
table = dynamodb.Table(table_name)

def create_game(event, context):
    """
    This API is called at the start of the application to create a new game.
    The user provides a length of the word to play with.
    A new game_id is generated and stored in the DynamoDB table userEntry with the provided word length.
    Returns the length of the word.
    """
    
    # Get the length of the word from the user's request
    word_length = int(event['n'])
    
    # Generate a new game ID
    game_id = str(uuid.uuid4())
    # Store the new game in DynamoDB
    table.put_item(Item={
        'id': str(uuid.uuid4()),
        'game_id': game_id,
        'word_length': word_length
    })
    
    # Return the length of the word to the user
    return word_length
