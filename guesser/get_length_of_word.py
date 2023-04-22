import json
import os
import random
import boto3
from boto3.dynamodb.conditions import Key, Attr

# This function would be used as a first step of the application
# User will tell the game the length of the word for wordle

def get_length_of_word(event, context):
   # print("Enter the length of the word for wordle:")
   # n = int(input("Enter the length of the word: "))
    n = int(event['n'])
    return n