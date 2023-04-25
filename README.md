## About the project

The aim of the project is to create a wordle game where the user can configure the word length of the target word. Depending on the word length,
the user can play wordle.

In wordle, user would enter the guess and we would check how close the guess is to the secret word. Depending on that, colors of tiles would change.

Green Color: Letter guessed at the right position.
Yellow Color: Correct letter, wrong position
Grey Color: Incorrect letter

According to these tiles, user would continue guessing until word length + 1 tries.


## Lambda functions

In this project, there are mainly two lambda functions used

### 1. create_game.py

Through this file, user would create a game by giving us the word length user would like to play with. That would be stored in a dynamoDB table with a game_id which is randomly generated. That game_id would be later used to match the secret word for the user. This is done so that the user can create multiple games at once.

### 2. guess_word.py 

In this file, user would enter "guess" and from the frontend side we would receive the game_id and the number of tries of user so far. That would be used to match the secret word the game uses so that we have correct word everytime.

## Testing this project 

I have tested it using AWS SAM. You can try out through anything else. 
These are the steps to be followed for testing through AWS SAM.

### Requirements
1. Install Docker
2. Install AWS CLI
3. Install AWS SAM

### Steps

1. After installing all of the above, open docker. This is the command used in mac: open -a Docker
2. After opening docker, go to the createGameTest directory in the terminal window. 
3. Run sam build, it should build succesfully. Make sure the python version matches your python version in the system in the template.yaml file.
4. After it is built, run the following: sam local invoke CreateGameFunction --event /Users/shreya/Desktop/wordle-app/test/createGameTest/nine-letter.json

Repeat similar steps for guessWordTest just change the paths and the function name. 

You should be able to get the desired output. 