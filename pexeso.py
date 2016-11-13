import tkinter


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.game = None
        self.new_game = None
        self.score = None
        self.quit = None
        self.canvas = None
        self.pack()
        self.initialize()

    def initialize(self):
        self.new_game = tkinter.Button(self)
        self.new_game["text"] = "New Game"
        self.new_game["command"] = self.create_new_game
        self.new_game.pack()
        self.score = tkinter.Label(self, text="Score: 0")
        self.score.pack()
        self.quit = tkinter.Button(self)
        self.quit["text"] = "Quit"
        self.quit["fg"] = "red"
        self.quit["command"] = self.master.quit
        self.quit.pack()
        self.canvas = tkinter.Canvas(self)
        self.canvas.pack()

    def create_new_game(self):
        self.game = Game()


class Game:
    def __init__(self):
        pass

    def canvas_clicked(self):
        pass


if __name__ == "__main__":
    app = Application()
    app.master.title("My first GUI app")
    app.master.maxsize(1000, 400)
    app.mainloop()
