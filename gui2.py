import tkinter as tk

AI1_Option = "aa"
AI2_Option = "aa"
AI1_Level = "bb"
AI2_Level = "bb"


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Connect4")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.thing1 = tk.Label(self, text="Choose AI1 Algorithm")
        self.thing1.pack()
        self.var1 = tk.StringVar(value="MinMax")
        self.option1_1 = tk.Radiobutton(self, text="MinMax", variable=self.var1, value="MinMax")
        self.option1_2 = tk.Radiobutton(self, text="AlphaBeta", variable=self.var1, value="AlphaBeta")
        self.option1_3 = tk.Radiobutton(self, text="Random", variable=self.var1, value="Random")
        self.option1_1.pack()
        self.option1_2.pack()
        self.option1_3.pack()

        self.thing2 = tk.Label(self, text="Choose AI1 Difficulty Level")
        self.thing2.pack()
        self.var2 = tk.StringVar(value="Hard")
        self.option2_1 = tk.Radiobutton(self, text="Hard", variable=self.var2, value="Hard")
        self.option2_2 = tk.Radiobutton(self, text="Medium", variable=self.var2, value="Medium")
        self.option2_3 = tk.Radiobutton(self, text="Easy", variable=self.var2, value="Easy")
        self.option2_1.pack()
        self.option2_2.pack()
        self.option2_3.pack()

        self.thing3 = tk.Label(self, text="Choose AI2 Algorithm")
        self.thing3.pack()
        self.var3 = tk.StringVar(value="MinMax")
        self.option3_1 = tk.Radiobutton(self, text="MinMax", variable=self.var3, value="MinMax")
        self.option3_2 = tk.Radiobutton(self, text="AlphaBeta", variable=self.var3, value="AlphaBeta")
        self.option3_3 = tk.Radiobutton(self, text="Random", variable=self.var3, value="Random")
        self.option3_1.pack()
        self.option3_2.pack()
        self.option3_3.pack()

        self.thing4 = tk.Label(self, text="Choose AI2 Difficulty Level")
        self.thing4.pack()
        self.var4 = tk.StringVar(value="Hard")
        self.option4_1 = tk.Radiobutton(self, text="Hard", variable=self.var4, value="Hard")
        self.option4_2 = tk.Radiobutton(self, text="Medium", variable=self.var4, value="Medium")
        self.option4_3 = tk.Radiobutton(self, text="Easy", variable=self.var4, value="Easy")
        self.option4_1.pack()
        self.option4_2.pack()
        self.option4_3.pack()

        self.submit = tk.Button(self, text="Start Game", command=self.selection)
        self.submit.pack()

    def selection(self):
        print("Thing 1:", self.var1.get())
        print("Thing 2:", self.var2.get())
        print("Thing 3:", self.var3.get())
        print("Thing 4:", self.var4.get())
        global AI1_Option
        AI1_Option = self.var1.get()
        global AI1_Level
        AI1_Level = self.var2.get()
        global AI2_Option
        AI2_Option = self.var3.get()
        global AI2_Level
        AI2_Level = self.var4.get()
        root.quit()


root = tk.Tk()
app = App(master=root)
app.mainloop()
