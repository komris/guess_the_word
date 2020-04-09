"""
Word Guessing Program, similar to hangman.
Created by Carl Gierisch, 2020
"""

#imports random module
import random

#List of words to be used in game
words = ["never", "sometimes", "refrigerator", "comma", "watermelon",\
"horseshoe", "altruistic", "centipede", "economy", "coronavirus",\
"rheumatoid", "alphabetical", "psyche", "physical", "congratulate",\
"contrived", "exposition", "bronchitis", "undulating", "irrelevent",\
"strawberry", "pineapple", "insubordinate", "insurance", "cataclysmic",\
"apostrophe", "jurassic", "principle", "smelly", "coordination", "potato",\
"synergistic", "colloquial", "college", "collage", "corpulent", "pimpernel",\
"scarlet"]

#Assigns secret_word as random word in list
secret_word = random.choice(words)

#Sets amount of guesses
guesses_left = 10


#creates a list with number of dashes needed for word, then joins them
dashes = []
word_list = list(secret_word)
for i in word_list:
    dashes.append("-")
dash = "".join(dashes)

#creates list for guessed letters
guess_list = []

#function to update dashes with correctly guessed letters
def update_dashes(secret_word, dashes, guess):
    for i in range(len(secret_word)):
        if guess == word_list[i]:
            dashes[i] = guess
    return "".join(dashes)

#function to get player guesses and inform whether correct
def get_guess(secret_word, guesses_left):
    while guesses_left > 0:
        print (str(guesses_left) + " incorrect guesses left.")
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print ("Your guess must have exactly one character!")
            continue
        if guess.isupper():
            print ("Your guess must be a lowercase letter!")
            continue
        elif guess in secret_word:
            print ("That letter is in the secret word!")
            return (guesses_left, guess)
        elif guess not in secret_word:
            print ("".join(dashes))
            guess_list.append(guess)
            print ("Incorrect Guesses: " + ",".join(guess_list))
            print ("That letter is not in the secret word!")
            guesses_left = guesses_left - 1
    return (guesses_left, guess)
            

#main program
print ("I'm thinking of a word with " + str(len(secret_word)) + " letters.")
print (dash)
while "".join(dashes) != secret_word and guesses_left != 0:
    (guesses_left, guess) = get_guess(secret_word, guesses_left)
    print (update_dashes(secret_word, dashes, guess))

if "".join(dashes) == secret_word:    
    print ("You win! The secret word was " + secret_word)
else:
    print ("You lose! The secret word was " + secret_word)
