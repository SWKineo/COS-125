import Tkinter

def contains(haystack, needle):
    """Returns True if all items in needle are also 
    found in haystack.Needle and haystick can be lists, 
    strings, or tuples"""
    for item in needle:
        if item not in haystack:
            return False
    return True


class cell:
    def __init__(self,cellNum,frame,game):
        self.button = Tkinter.Button(frame,
          text='?',
          command=self.makeMove,
          font=('Courier New',30),
          bg='white')
        self.button.pack(side='left')
        self.game = game
        self.value = '?'
        self.num = cellNum

    def makeMove(self):
        if self.value == '?':
            self.button.config(text=self.game.Player)
            self.value = self.game.Player
            self.game.updateGame(self.num)

    def restart(self):
        self.value = '?'
        self.button.config(bg='white')
        self.button.config(text='?')
        
    def freeze(self):
        if self.value == '?':
            self.value = ' '
            self.button.config(text=' ',
            bg='gray')

    def highlight(self):
       self.button.config(bg='green')
        

class TTTgame:
    def __init__(self):
        self.gameWin = Tkinter.Tk()
        #Replace the default tk title
        self.gameWin.title('TIC-TAC-TOE')
        
        #game state variables
        self.cells = [ ]     #game cells
        self.GameNum = 1     #game counter
        self.Player = 'X'    #current player
        self.free = range(9) #list of free cells
        #moves made are in a dictionary indexed by player
        self.moves = { 'X' : [ ], 'O' : [ ] }

        #create the game cells
        self.gameFrame = Tkinter.Frame(self.gameWin)
        self.cells = [ ]
        self.Row1 = Tkinter.Frame(self.gameWin)
        for i in range(3):
            self.cells.append(cell(i,self.Row1,self))
        self.Row2 = Tkinter.Frame(self.gameWin)
        for i in range(3,6):
            self.cells.append(cell(i,self.Row2,self))
        self.Row3 = Tkinter.Frame(self.gameWin)
        for i in range(6,9):
            self.cells.append(cell(i,self.Row3,self))

        self.topFrame = Tkinter.Frame(self.gameWin)
        self.countLabel = Tkinter.Label(self.topFrame,
          text='Playing Game 1',
          font=('Courier New',30),
          relief = 'raised',borderwidth=3)
        self.countLabel.pack()

        self.midFrame = Tkinter.Frame(self.gameWin)
        self.turnInfo = Tkinter.Label(self.midFrame,
          text=self.Player+' goes!',
          font=('Courier New',30))
        self.turnInfo.pack()
        self.botFrame = Tkinter.Frame(self.gameWin)
        self.quitBtn = Tkinter.Button(self.botFrame,
          text='Quit',
          command=self.gameWin.destroy,
          font=('Courier New',20))
        self.playBtn = Tkinter.Button(self.botFrame,
          text='Play Again',
          command=self.restart,
          font=('Courier New',20))
        self.quitBtn.pack(side='left')
        self.playBtn.pack(side='left')

        self.Row1.pack()
        self.Row2.pack()
        self.Row3.pack()
        self.gameFrame.pack()
        self.topFrame.pack()
        self.midFrame.pack()
        self.botFrame.pack()
        self.gameWin.mainloop()

    def won(self,Player):
        """return a list [Boolean,List] where Boolean is True
        if Player won, along with a list of the winning cells,
        returns [False,[]] otherwise"""
        winners = [
          [0,1,2],[3,4,5],[6,7,8],[0,3,6],
          [1,4,7],[2,5,8],[0,4,8],[2,4,6] ]
        for w in winners:
            if contains(self.moves[Player],w):
                return [True,w]
        return [False,[ ]]


    def updateGame(self, num):
        self.moves[self.Player].append(num)
        self.free.remove(num)
        w = self.won(self.Player)
        # remember that won returns values such as
        # [ True,[1,2,3] ]
        if w[0]:
            self.turnInfo.config(text=self.Player+' WON!')
            for c in self.cells:
                c.freeze()
            for i in w[1]:
                self.cells[i].highlight()
        elif self.free == [ ]:
            self.turnInfo.config(text='GAME IS A DRAW')
        else:
            if self.Player == 'X':
              self.Player = 'O'
            else:
                self.Player = 'X'
            self.turnInfo.config(
              text=self.Player+' goes!')
       

    def restart(self):
        #increment the game counter and reset all other vars
        self.GameNum += 1
        self.countLabel.config(text='Playing Game '+
          str(self.GameNum))
        self.Player = 'X'
        self.turnInfo.config(text=self.Player+' goes!')
        self.free = range(9)
        self.moves = { 'X' : [ ], 'O' : [ ] }
        for c in self.cells:
            c.restart()

TTT = TTTgame()
