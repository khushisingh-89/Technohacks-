import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TIC TAC TOE")
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 40), width=5, height=2, 
                                   command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

    def button_click(self, i, j):
        if self.buttons[i][j].cget("text") == "" and not self.check_winner():
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("TIC TAC TOE", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("TIC TAC TOE", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
      
        for i in range(3):
            if self.buttons[i][0].cget("text") == self.buttons[i][1].cget("text") == self.buttons[i][2].cget("text") != "":
                return True
        
        for j in range(3):
            if self.buttons[0][j].cget("text") == self.buttons[1][j].cget("text") == self.buttons[2][j].cget("text") != "":
                return True
        
        if self.buttons[0][0].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][2].cget("text") != "":
            return True
        if self.buttons[0][2].cget("text") == self.buttons[1][1].cget("text") == self.buttons[2][0].cget("text") != "":
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j].cget("text") == "":
                    return False
        return True

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()