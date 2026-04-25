import random
import tkinter as tk
from tkinter import messagebox

class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.min_num = 1
        self.max_num = 100
        self.max_attempts = 7

        self.reset_game()

        # UI Elements
        self.label_info = tk.Label(root, text="")
        self.label_info.pack(pady=10)

        self.entry_guess = tk.Entry(root)
        self.entry_guess.pack()

        self.button_guess = tk.Button(root, text="Guess", command=self.check_guess)
        self.button_guess.pack(pady=5)

        self.label_result = tk.Label(root, text="")
        self.label_result.pack(pady=10)

        self.button_restart = tk.Button(root, text="Restart", command=self.restart_game)
        self.button_restart.pack(pady=5)

        self.update_info()

    def reset_game(self):
        self.number = random.randint(self.min_num, self.max_num)
        self.attempts = 0

    def update_info(self):
        self.label_info.config(
            text=f"Guess a number between {self.min_num} and {self.max_num}\nAttempts left: {self.max_attempts - self.attempts}"
        )

    def check_guess(self):
        guess = self.entry_guess.get()

        if not guess.isdigit():
            self.label_result.config(text="Enter a valid number!")
            self.entry_guess.delete(0, tk.END)  # clear invalid input
            return

        guess = int(guess)
        self.attempts += 1

        if guess < self.number:
            self.label_result.config(text="Too low!")
        elif guess > self.number:
            self.label_result.config(text="Too high!")
        else:
            self.entry_guess.delete(0, tk.END)  # clear before popup
            play_again = messagebox.askyesno(
                "Success",
                f"Correct! You won in {self.attempts} attempts.\nDo you want to continue?"
            )

            if play_again:
                self.increase_difficulty()
            else:
                messagebox.showinfo("Exit", "Thanks for playing!")
                self.root.quit()
            return

        # LOSS CASE
        if self.attempts >= self.max_attempts:
            self.entry_guess.delete(0, tk.END)  # clear before popup
            play_again = messagebox.askyesno(
                "Game Over",
                f"You lost! Number was {self.number}\nDo you want to continue?"
            )

            if play_again:
                self.increase_difficulty()
            else:
                messagebox.showinfo("Exit", "Thanks for playing!")
                self.root.quit()
            return

        # 🔥 THIS is what you asked for: clear after every guess
        self.entry_guess.delete(0, tk.END)

        self.update_info()

    def increase_difficulty(self):
        self.max_num += 50
        self.reset_game()
        self.entry_guess.delete(0, tk.END)
        self.label_result.config(text="")
        self.update_info()

    def restart_game(self):
        self.min_num = 1
        self.max_num = 100
        self.reset_game()
        self.entry_guess.delete(0, tk.END)
        self.label_result.config(text="")
        self.update_info()


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGameGUI(root)
    root.mainloop()