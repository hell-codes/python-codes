import tkinter as tk
from tkinter import messagebox

board = [" " for _ in range(9)]
turn = "X"

wins = [
    (0,1,2), (3,4,5), (6,7,8),
    (0,3,6), (1,4,7), (2,5,8),
    (0,4,8), (2,4,6)
]

def check_win(player):
    return any(board[a]==board[b]==board[c]==player for a,b,c in wins)

def reset_game():
    global board, turn
    board = [" " for _ in range(9)]
    turn = "X"
    for button in buttons:
        button.config(text="", state="normal")

def on_click(i):
    global turn

    if board[i] == " ":
        board[i] = turn
        buttons[i].config(text=turn)

        if check_win(turn):
            messagebox.showinfo("Game Over", f"Player {turn} wins!")
            reset_game()
            return

        if " " not in board:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
            return

        turn = "O" if turn == "X" else "X"

# GUI setup
root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: on_click(i)
    )
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

reset_btn = tk.Button(root, text="Restart", font=("Arial", 14), command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()
