import random
import tkinter as tk

# List of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Select a random word
word = random.choice(words)

# Create the main window
root = tk.Tk()
root.title("Hangman Challenge")
root.geometry("500x500")

# Create a label to display the word
word_label = tk.Label(root, text="_ " * len(word), font=("Helvetica", 24))
word_label.pack()

# Create an entry field for the player's guess
guess_entry = tk.Entry(root, width=20)
guess_entry.pack()

# Create a label to display the number of incorrect guesses
guesses_label = tk.Label(root, text="Incorrect guesses: 0 / 6")
guesses_label.pack()

# Create a label to display the letters guessed so far
letters_label = tk.Label(root, text="Letters guessed: ")
letters_label.pack()

# Create a label to display the correctly guessed letters
correct_letters_label = tk.Label(root, text="Correct letters: ")
correct_letters_label.pack()

# Create a button to submit the guess
submit_button = tk.Button(root, text="Guess", command=lambda: guess_letter())
submit_button.pack()

# Create a button to restart the game
restart_button = tk.Button(root, text="Restart", command=lambda: restart_game())
restart_button.pack()

# Initialize game state
blank_spaces = ["_"] * len(word)
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []
correct_letters = []

def guess_letter():
    global incorrect_guesses, guessed_letters, correct_letters
    guess = guess_entry.get()
    guess_entry.delete(0, tk.END)
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                blank_spaces[i] = guess
                if guess not in correct_letters:
                    correct_letters.append(guess)
    else:
        incorrect_guesses += 1
        if guess not in guessed_letters:
            guessed_letters.append(guess)
    word_label.config(text=" ".join(blank_spaces))
    guesses_label.config(text=f"Incorrect guesses: {incorrect_guesses} / {max_guesses}")
    letters_label.config(text=f"Letters guessed: {', '.join(guessed_letters)}")
    correct_letters_label.config(text=f"Correct letters: {', '.join(correct_letters)}")
    check_win_loss()

def restart_game():
    global word, blank_spaces, incorrect_guesses, guessed_letters, correct_letters
    word = random.choice(words)
    blank_spaces = ["_"] * len(word)
    incorrect_guesses = 0
    guessed_letters = []
    correct_letters = []
    word_label.config(text="_ " * len(word))
    guesses_label.config(text="Incorrect guesses: 0 / 6")
    letters_label.config(text="Letters guessed: ")
    correct_letters_label.config(text="Correct letters: ")

def check_win_loss():
    if "_" not in blank_spaces:
        word_label.config(text="Congratulations, you won!")
        submit_button.config(state="disabled")
    elif incorrect_guesses == max_guesses:
        word_label.config(text=f"Sorry, you lost. The word was {word}")
        submit_button.config(state="disabled")

root.mainloop()