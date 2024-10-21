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
        result_label.config(text="Your guess is too low.", fg="red")
    elif guess > answer:
        result_label.config(text="Your guess is too high.", fg="red")
    else:
        result_label.config(text="Your guess is right! The answer was {}.".format(answer), fg="green")
        attempts_label.config(text="Congratulations! You won!", fg="green")
        secret_number_label.config(text="")

def game():
    window = tk.Tk()
    window.title("Guess the Number")
    window.geometry("500x500")
    window.configure(background="#f0f0f0")  # light gray background

    answer = random.randint(1, 50)
    attempts = 0
    difficulty = None

    # Create a title label with a bold font
    title_label = tk.Label(window, text="Guess the Number", font=("Arial", 24, "bold"), bg="#f0f0f0")
    title_label.pack(pady=20)

    # Create a frame for the difficulty level
    difficulty_frame = tk.Frame(window, bg="#f0f0f0")
    difficulty_frame.pack()

    difficulty_label = tk.Label(difficulty_frame, text="Choose a level of difficulty:", font=("Arial", 14), bg="#f0f0f0")
    difficulty_label.pack()

    def set_difficulty_easy():
        nonlocal attempts, difficulty
        difficulty = "easy"
        attempts = EASY_LEVEL_ATTEMPTS
        difficulty_label.config(text="You have chosen easy difficulty.", fg="blue")
        attempts_label.config(text="You have {} attempts remaining.".format(attempts), fg="blue")

    def set_difficulty_hard():
        nonlocal attempts, difficulty
        difficulty = "hard"
        attempts = HARD_LEVEL_ATTEMPTS
        difficulty_label.config(text="You have chosen hard difficulty.", fg="blue")
        attempts_label.config(text="You have {} attempts remaining.".format(attempts), fg="blue")

    easy_button = tk.Button(difficulty_frame, text="Easy", command=set_difficulty_easy, font=("Arial", 14), bg="#4CAF50", fg="white")
    easy_button.pack(side=tk.LEFT, padx=10)

    hard_button = tk.Button(difficulty_frame, text="Hard", command=set_difficulty_hard, font=("Arial", 14), bg="#4CAF50", fg="white")
    hard_button.pack(side=tk.LEFT, padx=10)

    # Create a frame for the guess input
    guess_frame = tk.Frame(window, bg="#f0f0f0")
    guess_frame.pack(pady=20)

    guess_label = tk.Label(guess_frame, text="Guess a number:", font=("Arial", 14), bg="#f0f0f0")
    guess_label.pack()

    guess_entry = tk.Entry(guess_frame, font=("Arial", 14), width=20)
    guess_entry.pack()

    result_label = tk.Label(guess_frame, text="", font=("Arial", 14), bg="#f0f0f0")
    result_label.pack()

    attempts_label = tk.Label(guess_frame, text="", font=("Arial", 14), bg="#f0f0f0")
    attempts_label.pack()

    secret_number_label = tk.Label(guess_frame, text="", font=("Arial", 14), bg="#f0f0f0")
    secret_number_label.pack()

    def check_answer_callback():
        nonlocal attempts
        if difficulty is None:
            result_label.config(text="Please choose a difficulty level first.", fg="red")
            return
        guess = int(guess_entry.get())
        check_answer(guess, answer, attempts, result_label, attempts_label, secret_number_label)
        attempts -= 1
        if attempts == 0:
            result_label.config(text="You are out of guesses. The correct answer was {}.".format(answer), fg="red")
            attempts_label.config(text="", fg="red")
        else:
            attempts_label.config(text="You have {} attempts remaining.".format(attempts), fg="blue")

    guess_button = tk.Button(guess_frame, text="Guess", command=check_answer_callback, font=("Arial", 14), bg="#4CAF50", fg="white")
    guess_button.pack(pady=10)

    window.mainloop()

game()
