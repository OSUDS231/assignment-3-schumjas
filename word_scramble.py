import random

# ----------------------------------------------------
# PROVIDED HELPER FUNCTIONS (DO NOT MODIFY)
# ----------------------------------------------------

def load_words(filename="words.txt"):
    """
    Loads the word list from a file and returns a list of words.
    Each word is assumed to be in lowercase.
    """
    print("Loading word list from file...")
    with open(filename, 'r') as f:
        wordlist = f.read().split()
    print(f"{len(wordlist)} words loaded")
    return wordlist

def choose_word(wordlist):
    """
    wordlist: list of strings
    returns: string, a randomly chosen word from the list
    """
    return random.choice(wordlist)

def scramble_word(secret_word):
    """
    Scrambles the letters of the given secret word and prints the scrambled version.
    Does not return anything.
    """
    letters = list(secret_word)
    random.shuffle(letters)
    scrambled = ''.join(letters)
    print(f"Scrambled word: {scrambled}")

# ----------------------------------------------------
# FUNCTIONS TO IMPLEMENT
# ----------------------------------------------------

# Task 1.1 
def input_check(secret_word):
    while True:
        guess = input("Your guess: ")
        guess2 = ''.join(i for i in guess if i.isalpha())
        guess2 = guess2.lower()
        if sorted(guess2) == sorted(secret_word):
            return guess2

# Task 1.2
def has_player_won(secret_word, user_guess):
    return secret_word == user_guess

# Task 1.3 
def get_word_progress(secret_word, user_guess):
    overlap = []
    for i in range(len(secret_word)):
        if secret_word[i] == user_guess[i]:
            overlap.append(secret_word[i])
        else:
            overlap.append("*")
    return ''.join(overlap)

# Task 2.1, 2.2 
def word_scramble():
    attempts = 5
    word_list = load_words()
    chosen = choose_word(word_list)
    print("Welcome to Word Scramble!")
    scramble_word(chosen)
    print(f"You have {attempts} attempts to guess the original word.")
    while attempts > 0:
        guess = input_check(chosen)
        if has_player_won(chosen, guess):
            print("You won!")
            print(f"You guessed the word with {attempts} attempt(s) remaining.")
            break
        else:
            attempts -= 1
            print(get_word_progress(chosen, guess))
    print(f"Sorry, you ran out of guesses. The word was {chosen}.")


if __name__ == "__main__":
    word_scramble()
