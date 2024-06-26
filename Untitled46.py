#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def guess_the_number():
    print("Welcome to the 'Guess the Number' game!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    guess = None
    number_of_guesses = 0
    
    while guess != number_to_guess:
        guess = input("Take a guess: ")
        
        # Ensure the guess is a valid number
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        number_of_guesses += 1
        
        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Congratulations! You've guessed the number in {number_of_guesses} tries.")

# Run the game
guess_the_number()


# In[ ]:




