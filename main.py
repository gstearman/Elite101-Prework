# C2C Chatbot project by GregS
import random

# Simple chat program
# Responds randomly with one of four preprogrammed responses
# TODO Add more questions abd related processing functions.

# This function plays guess the animal
def play_animal_game():
  print('TODO-Here is where we will play guess the animal.')

# This function generates a random response from a list of responses.
def generate_response(user_input):
  responses = [
    "How interesting!",
    "You don't say!",
    "Very cool!",
    "Programming is fun!"
  ]
  return random.choice(responses)

def init_chat():
  quit_character = 'q'

  user_input = input("Hello, how are you?\n")

  while user_input != quit_character:
    #Ask the user for more input, then use that in your response
    if "animal" in user_input:
      play_animal_game()
      # Get a new response from the user
      user_input = input("What else do you want to talk about?\n")
    else:
      user_input = input(generate_response(user_input) + "\n")

if __name__ == "__main__":
  init_chat()
  print('Goodbye and thanks for talking.')