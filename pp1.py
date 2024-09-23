import random
import tkinter as tk

# Set difficulty levels
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level):
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level == "hard":
        return HARD_LEVEL_ATTEMPTS
    else:
        print("Invalid difficulty level. Please choose easy or hard.")
        return None

def check_answer(guess, answer, attempts, result_label, attempts_label, secret_number_label):
    if guess < answer:
        result_label.config(text="Your guess is too low.")
    elif guess > answer:
        result_label.config(text="Your guess is too high.")
    else:
        result_label.config(text="Your guess is right! The answer was {}.".format(answer))
        attempts_label.config(text="Congratulations! You won!")
        secret_number_label.config(text="")

def game():
    window = tk.Tk()
    window.title("Guess the Number")
    window.geometry("500x500")

    answer = random.randint(1, 50)
    attempts = 0
    difficulty = None

    difficulty_label = tk.Label(window, text="Choose a level of difficulty:")
    difficulty_label.pack()

    difficulty_frame = tk.Frame(window)
    difficulty_frame.pack()

    def set_difficulty_easy():
        nonlocal attempts, difficulty
        difficulty = "easy"
        attempts = EASY_LEVEL_ATTEMPTS
        difficulty_label.config(text="You have chosen easy difficulty.")
        attempts_label.config(text="You have {} attempts remaining.".format(attempts))

    def set_difficulty_hard():
        nonlocal attempts, difficulty
        difficulty = "hard"
        attempts = HARD_LEVEL_ATTEMPTS
        difficulty_label.config(text="You have chosen hard difficulty.")
        attempts_label.config(text="You have {} attempts remaining.".format(attempts))

    easy_button = tk.Button(difficulty_frame, text="Easy", command=set_difficulty_easy)
    easy_button.pack(side=tk.LEFT)

    hard_button = tk.Button(difficulty_frame, text="Hard", command=set_difficulty_hard)
    hard_button.pack(side=tk.LEFT)

    guess_label = tk.Label(window, text="Guess a number:")
    guess_label.pack()

    guess_entry = tk.Entry(window)
    guess_entry.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    attempts_label = tk.Label(window, text="")
    attempts_label.pack()

    secret_number_label = tk.Label(window, text="")
    secret_number_label.pack()

    def check_answer_callback():
        nonlocal attempts
        if difficulty is None:
            result_label.config(text="Please choose a difficulty level first.")
            return
        guess = int(guess_entry.get())
        check_answer(guess, answer, attempts, result_label, attempts_label, secret_number_label)
        attempts -= 1
        if attempts == 0:
            result_label.config(text="You are out of guesses. The correct answer was {}.".format(answer))
            #secret_number_label.config(text="Secret number: {}".format(answer))
            attempts_label.config(text="")
        else:
            attempts_label.config(text="You have {} attempts remaining.".format(attempts))

    guess_button = tk.Button(window, text="Guess", command=check_answer_callback)
    guess_button.pack()

    window.mainloop()

game()