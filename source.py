import random

# list of words to choose from
word_list = ["python", "javascript", "programming", "computer", "science"]

# randomly select a word from the list
word = random.choice(word_list)

# create a list to store the letters that have been guessed
guessed_letters = []

# create a variable to keep track of the number of wrong guesses
wrong_guesses = 0

while wrong_guesses < 6:
    # create a variable to keep track of whether the player has won
    win = True

    # create a variable to store the current state of the word (with unguessed letters replaced by _)
    word_display = ""
    for letter in word:
        if letter in guessed_letters:
            word_display += letter
        else:
            word_display += "_"
            win = False

    # print the current state of the word
    print(word_display)

    # if the player has won, print a message and break out of the loop
    if win:
        print("Congratulations, you win!")
        break

    # prompt the player to guess a letter
    guess = input("Guess a letter: ")

    # if the player has already guessed this letter, print a message and continue the loop
    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    # add the letter to the list of guessed letters
    guessed_letters.append(guess)

    # if the letter is not in the word, increment the number of wrong guesses
    if guess not in word:
        wrong_guesses += 1
        print("Incorrect. You have", 6 - wrong_guesses, "guesses left.")
    else:
        print("Correct!")

# if the player has used up all their guesses, print a message
if wrong_guesses == 6:
    print("Sorry, you lose. The word was", word + ".")
