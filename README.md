# Hangman-Game

1 - First, we import the random module, which we will use later to randomly select a word from our list of words.

2 - Next, we create a list of words called word_list that the game will randomly choose from. You can replace these words with your own list of words.

3 - We use the random.choice() function to randomly select a word from the word_list and store it in the word variable.

4 - We create an empty list called guessed_letters to store the letters that the player has guessed. We also create a variable wrong_guesses and set it to 0,
which we will use to keep track of the number of wrong guesses the player has made.

5 - The code then enters a while loop that runs as long as wrong_guesses is less than 6. This means the player has 6 chances to guess the word.

6 - Within the while loop, we create a variable win and set it to True. We also create another variable word_display, which we will use to store the current state of the word,
with unguessed letters replaced by underscores.

7 - Then we iterate through each letter of the word and checks if it is in the list of guessed letters. If it is, we add that letter to the word_display variable, otherwise,
we add an underscore. If there is any underscore remaining in the word_display variable, we set the win variable to False.

8 - After the word_display variable is constructed, we print it so the player can see the current state of the word. If win is True,
it means that the player has guessed all the letters in the word and we print a message saying that the player wins and break the loop.

9 - If the player has not won yet, we prompt the player to guess a letter. We check if the letter has already been guessed and if so, we print a message and continue the loop without incrementing the number of wrong guesses. If the letter has not been guessed yet, we add it to the list of guessed letters.

10 - Next, we check if the letter is in the word, if it is not then we increment the number of wrong guesses by 1. We also print a message telling the player how many guesses they have left. If the letter is in the word, we print a message saying the guess is correct.

11 - If the loop completes and the player has used all their guesses, we print a message saying that the player loses and what the word was.
