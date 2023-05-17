import tkinter as tk
from tkinter import messagebox

def open_level_window():
    level_window = tk.Toplevel(main_window)
    level_window.title("Select Level")
    level_window.geometry("400x400")

    level_label = tk.Label(level_window, text="Select the level:")
    level_label.pack(pady=10)

    level_var = tk.StringVar()

    level_easy = tk.Radiobutton(level_window, text="Easy", variable=level_var, value="easy")
    level_easy.pack()
    level_medium = tk.Radiobutton(level_window, text="Medium", variable=level_var, value="medium")
    level_medium.pack()
    level_hard = tk.Radiobutton(level_window, text="Hard", variable=level_var, value="hard")
    level_hard.pack()

    level_button = tk.Button(level_window, text="Start Game", command=lambda: start_game(level_var.get()))
    level_button.pack(pady=10)

def start_game(level=None):
    # Game logic goes here
    if level:
        messagebox.showinfo("Game Started", f"Game started with {level} level")
    else:
        messagebox.showinfo("Game Started", "Game started")

def open_game_window():
    game_window = tk.Toplevel(main_window)
    game_window.title("Choose Algorithm")
    game_window.geometry("400x400")

    player1_label = tk.Label(game_window, text="Player 1:")
    player1_label.pack(pady=10)

    player1_algorithm_var = tk.StringVar()

    player1_minmax = tk.Radiobutton(game_window, text="Min Max", variable=player1_algorithm_var, value="minmax")
    player1_minmax.pack()
    player1_alphabeta = tk.Radiobutton(game_window, text="Alpha Beta", variable=player1_algorithm_var, value="alphabeta")
    player1_alphabeta.pack()
    player1_random = tk.Radiobutton(game_window, text="Random", variable=player1_algorithm_var, value="random")
    player1_random.pack()

    player2_label = tk.Label(game_window, text="Player 2:")
    player2_label.pack(pady=10)

    player2_algorithm_var = tk.StringVar()

    player2_minmax = tk.Radiobutton(game_window, text="Min Max", variable=player2_algorithm_var, value="minmax")
    player2_minmax.pack()
    player2_alphabeta = tk.Radiobutton(game_window, text="Alpha Beta", variable=player2_algorithm_var, value="alphabeta")
    player2_alphabeta.pack()
    player2_random = tk.Radiobutton(game_window, text="Random", variable=player2_algorithm_var, value="random")
    player2_random.pack()

    def start_game_with_levels():
        algorithm1 = player1_algorithm_var.get()
        algorithm2 = player2_algorithm_var.get()

        if algorithm1 == "alphabeta" or algorithm2 == "alphabeta":
            open_level_window()
        else:
            start_game()

    algorithm_button = tk.Button(game_window, text="Start", command=start_game_with_levels)
    algorithm_button.pack(pady=10)

# Create the main window
main_window = tk.Tk()
main_window.title("Game Setup")
main_window.geometry("400x400")

# Create the label and button for starting the game
start_label = tk.Label(main_window,
text="Click the button to start the game:")
start_label.pack(pady=10)

start_button = tk.Button(main_window, text="Start Game", command=open_game_window)
start_button.pack(pady=10)

main_window.mainloop()

