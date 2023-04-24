import boto3
from boto3.dynamodb.conditions import Key


def get_word_length(game_id):
    """
    Retrieves the word length for a given game_id from the DynamoDB table userEntry.
    Returns the word length as an integer.
    """
    
    dynamodb = boto3.resource('dynamodb')
    table_name = 'userEntry'
    table = dynamodb.Table(table_name)
    response = table.query(
        IndexName='game_id_index',
        KeyConditionExpression=Key('game_id').eq(game_id),
        ProjectionExpression='word_length'
    )
    items = response.get('Items', [])
    if len(items) == 0:
        raise ValueError(f"No matching item found for game_id {game_id}")
    n = int(items[0]['word_length'])
    return n
