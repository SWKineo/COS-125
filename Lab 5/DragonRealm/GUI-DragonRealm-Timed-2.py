"""This version uses the time.time() method
to perform a timed action and impart a sense
of drama to the game"""

from Tkinter import *
import random
import time

def wait(seconds):
    """ wait loops (a "busy wait") until
    specified seconds have passed. 
    Seconds can be a float"""
    # get current time in seconds
    now  = time.time() 
    when = now + seconds
    while time.time() < when:
        pass  #pass is "do nothing"

def Spacer():
    return Label(win,text=' ',font=fontn)

win = Tk()
win.title('Dragon Realm')
fontn = ('Courier New',30)
fontb = fontn + ('bold',)


introStr = """
You are on a planet
full of dragons.
In front of you
are two caves.
In one cave,
the dragon is friendly
and will share his
treasure with you.
The other dragon is greedy
and hungry, and will eat
you on sight. If you
decide to play you will
have to choose one of
the two caves to enter!
"""

gameState = 0
GoodCave = 0
userSel = 0

def button1():
    global gameState, userSel
    if gameState == 1:
        userSel = 1
        gameState = 2
        showGame(2)
        
def button2():
    global gameState, userSel
    if gameState == 1:
        userSel = 2
        gameState = 2
        showGame(2)
        
def play():
    global gameState, userSel, GoodCave, Pic, Cap
    if gameState == 0:
        gameState = 1
        showGame(1)
    elif gameState == 2:
        gameState = 3
        if userSel == GoodCave:
            Pic = goodDragon
            Cap = "Gives you his treasure!"
        else:
            Pic = badDragon
            Cap = "Gobbles you down in one bite!"
        showGame(3)
    elif gameState == 3:
        gameState = 0
        showGame(0)

def timedLabel():
    """Display text progressively on the center label
    using wait() to wait two seconds between each line"""
    ttxt = "You approach the cave ..." + '\n' * 7
    centerLabel.config(text=ttxt)
    win.update() #force a screen update
    wait(2)    
    ttxt = "You approach the cave ...\n\n"\
        +"It is dark and spooky..."+ '\n' * 5
    centerLabel.config(text=ttxt)
    win.update()
    wait(2)
    ttxt = "You approach the cave ...\n\n"\
        +"It is dark and spooky..."\
        +"\n\nA large dragon jumps out\n"\
        +"in front of you!"+ '\n' * 2  
    centerLabel.config(text=ttxt)
    win.update()
    wait(2)
    ttxt = "You approach the cave ...\n\n"\
        +"It is dark and spooky..."\
        +"\n\nA large dragon jumps out\n"\
        +"in front of you!"\
        +'\n\nHe opens his jaws and ...'
    centerLabel.config(text=ttxt)
    playBtn.config(text='CONTINUE')
    win.update()
              
    
def showGame(gameState):
    global Pic, Cap, GoodCave
    if gameState == 0:
        dragonPic.grid_remove()
        resultLabel.grid_remove()
        playBtn.config(text='PLAY')
        playBtn.grid(row=3,column=3)
        leftButton.config(image=Globe)
        leftButton.grid(row=1,column=1)
        rghtButton.config(image=Globe)
        rghtButton.grid(row=1,column=5)
        centerLabel.config(text=introStr,font=('Courier New',18))
        centerLabel.grid(row=1,column=3)
        GoodCave = random.randint(1,2)
    elif gameState == 1:
        playBtn.grid_remove()
        leftButton.config(image=Lcave)
        rghtButton.config(image=Rcave)
        centerLabel.config(text='Choose a Cave',font=fontb)
    elif gameState == 2:
        leftButton.grid_remove()
        rghtButton.grid_remove()
        playBtn.grid(row=3,column=3)
        playBtn.config(text='uh oh...')
        timedLabel()
    elif gameState == 3:
        centerLabel.grid_remove()
        dragonPic.config(image=Pic)
        dragonPic.grid(row=1,column=3)
        resultLabel.config(text=Cap)
        resultLabel.grid(row=0,column=3)
        
        playBtn.config(text='PLAY AGAIN')

# Start of main()
# Layout the screen
for i in range(7):
    Spacer().grid(row=0,column=i)
    Spacer().grid(row=2,column=i)
    Spacer().grid(row=5,column=i)
Globe = PhotoImage(file='Globe.gif')
Lcave = PhotoImage(file='CaveLeft.gif')
Rcave = PhotoImage(file='CaveRight.gif')
badDragon  = PhotoImage(file='FierceDragon.gif')
goodDragon = PhotoImage(file='FriendlyDragon.gif')
Pic = goodDragon
Cap = "Gives you his treasure!"


quitBtn = Button(win,text='QUIT',font=fontb,command=win.destroy,width=12)
quitBtn.grid(row=4,column=3)
playBtn = Button(win,text='PLAY',font=fontb,width=12,command=play)
leftButton = Button(win,image=Globe,font=fontb,command=button1)
rghtButton = Button(win,image=Globe,font=fontb,command=button2)
centerLabel = Label(win,text=introStr,justify='left',font=('Courier New',18))
dragonPic = Label(win,image=Globe)
resultLabel = Label(win,text="Not Changed",font=fontb)

showGame(0)

win.mainloop()
