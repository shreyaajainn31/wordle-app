import json
import os
import random
import boto3
from boto3.dynamodb.conditions import Key, Attr
from get_random_word import get_random_word
import uuid

def get_secret_word(game_id):
    """
    
    This function would first check if the game_id is already present
    in the secretWordTable.
    If it is, it would get the corresponding word from that table
    and return that.
    Otherwise, it would call the get_random_word function to get the 
    random word and return that word
    
    """
    dynamodb = boto3.resource('dynamodb')
    table_name = 'secretWordTable'
    table = dynamodb.Table(table_name)
    response = table.query(
        IndexName='game_id-index',
        KeyConditionExpression=Key('game_id').eq(game_id)
    )
    items = response.get('Items', [])
    if len(items) > 0:
        return items[0]['word']
    else:
        word = get_random_word(game_id)
        secret_word_id = str(uuid.uuid4())
        item = {
            "id": secret_word_id,
            "game_id": game_id,
            "word": word
        }
        table.put_item(Item=item)
        return word
