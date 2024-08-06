import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        # Make the window full screen
        self.root.geometry("700x750")  # Updated window size
        self.root.configure(bg='lightblue') 

        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self.scores = {"X": 0, "O": 0}  # Initialize scores for X and O
        
        self.create_widgets()

    def create_widgets(self):
        # Score labels
        self.score_x_label = tk.Label(self.root, text=f"Player X: {self.scores['X']}", font=("Arial", 16), bg='lightblue')
        self.score_x_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.score_o_label = tk.Label(self.root, text=f"Player O: {self.scores['O']}", font=("Arial", 16), bg='lightblue')
        self.score_o_label.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        
        # Center the score labels in their row
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Create game board
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Arial", 32), width=6, height=3,  # Increased font size and button size
                               bg='white', fg='black', activebackground='lightgray',
                               command=lambda i=i: self.make_move(i))
            button.grid(row=(i // 3) + 1, column=i % 3, padx=10, pady=10)  # Shift buttons down by 1 row
            self.buttons.append(button)
        
        # Center game board in the window
        for i in range(3):
            self.root.grid_rowconfigure(i + 1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Scores", font=("Arial", 16), command=self.reset_scores)
        self.reset_button.grid(row=4, column=1, padx=10, pady=10, sticky="n")
        
        # Center the reset button in its row
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def make_move(self, index):
        if self.board[index] == " " and not self.check_win(self.current_player) and not self.check_tie():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, bg='lightgreen' if self.current_player == "X" else 'lightcoral')
            
            if self.check_win(self.current_player):
                self.scores[self.current_player] += 1  # Update the score for the winning player
                self.score_x_label.config(text=f"Player X: {self.scores['X']}")
                self.score_o_label.config(text=f"Player O: {self.scores['O']}")
                self.end_game(f"Player {self.current_player} wins!")
            elif self.check_tie():
                self.end_game("It's a tie!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_win(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] == player:
                return True
        return False

    def check_tie(self):
        return all(space != " " for space in self.board)

    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.reset_game()

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ", bg='white')

    def reset_scores(self):
        self.scores = {"X": 0, "O": 0}
        self.score_x_label.config(text=f"Player X: {self.scores['X']}")
        self.score_o_label.config(text=f"Player O: {self.scores['O']}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
