import tkinter as tk
from tkinter import messagebox
import random


def start_game():
    global secret_number
    secret_number = random.randint(1, 100)
    guess_button['state'] = 'normal'
    feedback_label['text'] = "Guess a number between 1 and 100"
    guess_entry.delete(0, tk.END)
def make_guess():
    try:
        guess = int(guess_entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return
    if guess < secret_number:
        feedback_label['text'] = "Too low! Try again."
    elif guess > secret_number:
        feedback_label['text'] = "Too high! Try again."
    else:
        messagebox.showinfo("Congratulations!", "You've guessed the number!")
        guess_button['state'] = 'disabled'
        feedback_label['text'] = "Game over. Start a new game to play again."
root = tk.Tk()
root.title("Number Guessing using Python")
secret_number = random.randint(1, 100)
title_label = tk.Label(root, text="Number Guessing Game", font=("TimesNew Roman", 16))
title_label.pack(pady=12)
feedback_label = tk.Label(root, text="Guess a number between 1 and 100", font=("TimesNew Roman", 12))
feedback_label.pack(pady=12)
guess_entry = tk.Entry(root, font=("TimesNew Roman", 14))
guess_entry.pack(pady=12)
guess_button = tk.Button(root, text="Submit Guess", command=make_guess, font=("TimesNew Roman", 12))
guess_button.pack(pady=12)
new_game_button = tk.Button(root, text="New Game", command=start_game, font=("TimesNew Roman", 12))
new_game_button.pack(pady=12)
root.mainloop()
