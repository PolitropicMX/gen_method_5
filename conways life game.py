import tkinter as tk
import random

class ConwayGame:
    def __init__(self, master, rows, columns):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.board = [[random.choice([0, 1]) for _ in range(columns)] for _ in range(rows)]
        self.buttons = [[None] * columns for _ in range(rows)]
        self.create_widgets()

    def create_widgets(self):
        for i in range(self.rows):
            for j in range(self.columns):
                btn = tk.Button(self.master, width=2, height=1, command=lambda i=i, j=j: self.toggle_cell(i, j))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn
                self.update_button_color(i, j)

        start_button = tk.Button(self.master, text="Start", command=self.start_game)
        start_button.grid(row=self.rows, column=0, columnspan=self.columns, pady=10)

    def toggle_cell(self, i, j):
        self.board[i][j] = 1 - self.board[i][j]
        self.update_button_color(i, j)

    def update_button_color(self, i, j):
        color = "black" if self.board[i][j] else "white"
        self.buttons[i][j].configure(bg=color)

    def start_game(self):
        for _ in range(100):
            self.update_board()
            self.master.after(200)
            self.master.update()

    def count_neighbors(self, i, j):
        count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                ni, nj = i + x, j + y
                if 0 <= ni < self.rows and 0 <= nj < self.columns and self.board[ni][nj]:
                    count += 1
        return count

    def update_board(self):
        new_board = [[0] * self.columns for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                neighbors = self.count_neighbors(i, j)
                if self.board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        new_board[i][j] = 0
                    else:
                        new_board[i][j] = 1
                elif neighbors == 3:
                    new_board[i][j] = 1

        self.board = new_board
        for i in range(self.rows):
            for j in range(self.columns):
                self.update_button_color(i, j)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Conway's Game of Life")
    game = ConwayGame(root, rows=20, columns=20)
    root.mainloop()
