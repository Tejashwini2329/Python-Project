import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

def create_password_generator():
    root = tk.Tk()
    root.title("Secure Password Generator")
    root.geometry("500x500")

    tk.Label(root, text="Password Length:").grid(row=0, column=0)
    length_entry = tk.Entry(root)
    length_entry.grid(row=0, column=1)

    tk.Label(root, text="Include Uppercase Letters:").grid(row=1, column=0)
    uppercase_var = tk.BooleanVar()
    tk.Checkbutton(root, variable=uppercase_var).grid(row=1, column=1)

    tk.Label(root, text="Include Numbers:").grid(row=2, column=0)
    numbers_var = tk.BooleanVar()
    tk.Checkbutton(root, variable=numbers_var).grid(row=2, column=1)

    tk.Label(root, text="Include Symbols:").grid(row=3, column=0)
    symbols_var = tk.BooleanVar()
    tk.Checkbutton(root, variable=symbols_var).grid(row=3, column=1)

    def generate_password():
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        characters = string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        password_label.config(text=password)

    tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2)

    tk.Label(root, text="Generated Password:").grid(row=5, column=0)
    password_label = tk.Label(root, text="")
    password_label.grid(row=5, column=1)

    def copy_to_clipboard():
        password = password_label.cget("text")
        pyperclip.copy(password)
        messagebox.showinfo("Password Copied", "Password copied to clipboard.")

    tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2)

    root.mainloop()

if __name__ == "__main__":
    create_password_generator()