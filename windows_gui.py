import tkinter as tk

AI1_Option = "aa"
AI2_Option = "aa"
# AI1_Level = "bb"
# AI2_Level = "bb"

#main->game ->level

def LevelWindow():

    level_window = tk.Toplevel(main_window)
    level_window.title("Select Level")
    level_window.geometry("400x400")

    level_label = tk.Label(level_window, text="Select the level:")
    level_label.pack(pady=10)

    level_var = tk.StringVar()
    level_var.set("Easy")
    level_easy = tk.Radiobutton(level_window, text="Easy", variable=level_var, value="Easy")
    level_easy.pack()
    level_medium = tk.Radiobutton(level_window, text="Medium", variable=level_var, value="Medium")
    level_medium.pack()
    level_hard = tk.Radiobutton(level_window, text="Hard", variable=level_var, value="Hard")
    level_hard.pack()

    level_button = tk.Button(level_window, text="Start Game", command=lambda: start_game())
    level_button.pack(pady=10)
    #print(level_var.get() + "    llllllooolooooooooo")
    return level_var.get()

def start_game():
    main_window.quit()
    #main_window.close()

def GameWindow():
    main_window.withdraw()
    game_window = tk.Toplevel(main_window)
    game_window.title("Choose Algorithm")
    game_window.geometry("400x400")

    player1_label = tk.Label(game_window, text="Player 1:")
    player1_label.pack(pady=10)

    player1_algorithm_var = tk.StringVar()
    player1_algorithm_var.set("MinMax")
    player1_minmax = tk.Radiobutton(game_window, text="MinMax", variable=player1_algorithm_var, value="MinMax")
    player1_minmax.pack()
    player1_alphabeta = tk.Radiobutton(game_window, text="AlphaBeta", variable=player1_algorithm_var, value="AlphaBeta")
    player1_alphabeta.pack()
    player1_random = tk.Radiobutton(game_window, text="Random", variable=player1_algorithm_var, value="Random")
    player1_random.pack()

    player2_label = tk.Label(game_window, text="Player 2:")
    player2_label.pack(pady=10)

    player2_algorithm_var = tk.StringVar()
    player2_algorithm_var.set("MinMax")

    player2_minmax = tk.Radiobutton(game_window, text="MinMax", variable=player2_algorithm_var, value="MinMax")
    player2_minmax.pack()
    player2_alphabeta = tk.Radiobutton(game_window, text="AlphaBeta", variable=player2_algorithm_var, value="AlphaBeta")
    player2_alphabeta.pack()
    player2_random = tk.Radiobutton(game_window, text="Random", variable=player2_algorithm_var, value="Random")
    player2_random.pack()

    def selectOption():
        algorithm1 = player1_algorithm_var.get()
        algorithm2 = player2_algorithm_var.get()
        global AI1_Option
        AI1_Option = algorithm1
        global AI2_Option
        AI2_Option = algorithm2

        #if AI1_Option == "AlphaBeta":
            # global AI1_Level
            # AI1_Level = LevelWindow()
            # global AI2_Level
            # AI2_Level = "Hard"

        #if AI2_Option == "AlphaBeta":
            # global AI2_Level
            # AI2_Level = LevelWindow()
            # global AI1_Level
            # AI1_Level = "Hard"

        if AI2_Option != "AlphaBeta" and AI1_Option != "AlphaBeta":
            start_game()
            # global AI1_Level
            # AI1_Level = "Hard"
            # global AI2_Level
            # AI2_Level = "Hard"

        #print(AI1_Option + "   " + AI2_Option + "  " + str(AI1_Level) + "  " + str(AI2_Level) + " ***********************************")



    algorithm_button = tk.Button(game_window, text="Start", command=selectOption)
    algorithm_button.pack(pady=10)

# Create the main window

main_window = tk.Tk()
main_window.title("Game Setup")
main_window.geometry("400x400")

# Create the label and button for starting the game
start_label = tk.Label(main_window,
text="Click the button to start the game:")
start_label.pack(pady=10)

start_button = tk.Button(main_window, text="Start Game", command=GameWindow())
start_button.pack(pady=10)

main_window.mainloop()
