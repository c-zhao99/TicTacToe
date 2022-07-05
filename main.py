import random
import tkinter
from tkinter import messagebox

#commit check

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol


class Square:
    def __init__(self):
        self.player = None

    def clear(self):
        self.player = None

    def change(self, player):
        self.player = player

    def getPlayer(self):
        return self.player


class Game:
    def __init__(self):
        self.board = []
        self.winner = None
        self.p1 = Player("Player 1", "X")
        self.p2 = Player("Player 2", "O")
        startingPlayer = random.randint(1, 2)
        if startingPlayer == 1:
            self.turn = self.p1
        else:
            self.turn = self.p2
        for i in range(3):
            row = []
            for j in range(3):
                row.append(Square())
            self.board.append(row)

    def checkRow(self, row):
        if self.board[row][0].getPlayer() == self.board[row][1].getPlayer() and \
                self.board[row][1].getPlayer() == self.board[row][2].getPlayer() and self.board[row][0].getPlayer() is not None:
            self.winner = self.board[row][0].getPlayer().getName()
            return True
        else:
            return False

    def checkColumn(self, column):
        if self.board[0][column].getPlayer() == self.board[1][column].getPlayer() and \
                self.board[1][column].getPlayer() == self.board[2][column].getPlayer() and self.board[0][column].getPlayer() is not None:
            self.winner = self.board[0][column].getPlayer().getName()
            return True
        else:
            return False

    def checkDiagonal1(self):
        if self.board[0][0].getPlayer() == self.board[1][1].getPlayer() and self.board[1][1].getPlayer() == self.board[2][2].getPlayer()\
                and self.board[0][0].getPlayer() is not None:
            self.winner = self.board[0][0].getPlayer().getName()
            return True
        else:
            return False

    def checkDiagonal2(self):
        if self.board[0][2].getPlayer() == self.board[1][1].getPlayer() and self.board[1][1].getPlayer() == \
                self.board[2][0].getPlayer() \
                and self.board[0][2].getPlayer() is not None:
            self.winner = self.board[0][2].getPlayer().getName()
            return True
        else:
            return False

    def checkEnd(self):
        if self.checkDiagonal1() or self.checkDiagonal2():
            return True
        else:
            for i in range(3):
                if self.checkRow(i) or self.checkColumn(i):
                    return True
            return False

    def changeTurn(self):
        if self.turn == self.p1:
            self.turn = self.p2
        else:
            self.turn = self.p1

    def action(self, row, column):
        self.board[row][column].change(self.turn)
        self.changeTurn()
        return self.checkEnd()




class MyButton(tkinter.Button):
    def __init__(self, master, row, column, label, game, window, **kw):
        tkinter.Button.__init__(self, master=master, command=self.command, **kw)
        self.game = game
        self.label = label
        self.row = row
        self.column = column
        self.defaultBackground = self["background"]
        self.window = window
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        if self['state'] != tkinter.DISABLED:
            self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

    def command(self):
        self['state'] = tkinter.DISABLED
        self['text'] = self.game.turn.getSymbol()
        self['font'] = ('Helvetica', 30)
        if self.game.action(self.row, self.column):
            messagebox.showinfo("End game", self.game.winner + " has won")
            self.window.destroy()
        else:
            self.label['text'] = self.game.turn.getName() + "'s turn"





def main():




    n = 1
    while True:

        game = Game()
        window = tkinter.Tk()
        legend1 = tkinter.Label(text=game.p1.getName() + " = " + game.p1.getSymbol())
        legend2 = tkinter.Label(text=game.p2.getName() + " = " + game.p2.getSymbol())
        legend1.pack()
        legend2.pack()
        label = tkinter.Label()
        label['text'] = game.turn.getName() + "'s turn"
        label.pack()
        main = tkinter.Frame(master=window)
        main.pack()

        for i in range(3):
            for j in range(3):
                frame = tkinter.Frame(main, height=100, width=100)
                button = MyButton(frame, i, j, label, game, window, activebackground='yellow')
                frame.grid_propagate(False)
                frame.columnconfigure(0, weight=1)
                frame.rowconfigure(0, weight=1)
                frame.grid(row=i, column=j)
                button.grid(sticky="wens")

        window.mainloop()
        print("Game " + str(n) + " has ended")
        n+=1


if __name__ == "__main__":
    main()


