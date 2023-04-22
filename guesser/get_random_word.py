import json
import os
import random
import boto3
from boto3.dynamodb.conditions import Key, Attr
from guesser.get_length_of_word import get_length_of_word

# This function would fetch the words from the table
# We would give n as a parameter, which is length of the word, and 
# in return send a random word of length n

def get_random_word():
    n = get_length_of_word()
    response = table.query(
        IndexName='word_length_index',
        KeyConditionExpression=Key('word_length').eq(n),
        ProjectionExpression='word'
    )

    words = [item['word'] for item in response['Items']]

    if words:
        return random.choice(words)
    else:
        return None