"""Christopher Birden, COS 125 Fall 2016 HW #3"""
import Tkinter
import random

class Hand:

    def roll_dice(self):
        for i in range(5):
            self.dice[i].roll()

class Die:
    def __init__(self, frame):
       self.value = random.randint(1,6)
       img = Tkinter.PhotoImage(file='1.gif')
       self.display = Tkinter.Label(frame,
                                    image=img,
                                    relief = 'ridge',
                                    borderwidth = 6)
       self.display.pack(side = 'left'),

    def roll(self):
        self.value = random.randint(1,6)
        self.display.config(image = Tkinter.PhotoImage(file = str(self.value)+ '.gif'))


class Diceroller:
    def __init__(self):
        dice_win = Tkinter.Tk()
        dice_win.title('Roll The Dice')
        dice_frame = Tkinter.Frame(dice_win)
        self.dice = []
        for i in range(5):
            self.dice.append(Die(dice_frame))
        roll_button = Tkinter.Button(dice_win,
                                     text = 'Roll again?',
                                     command = self.roll_dice,
                                     font = ('Times New Roman', 30),
                                     relief = 'raised',
                                     borderwidth = 6,
                                     width = 10)
        dice_frame.pack()
        roll_button.pack(side = 'bottom')
        separator = Tkinter.Frame(height=2, bd=1, relief='sunken')
        separator.pack(fill='x', padx=5, pady=5)
        dice_win.mainloop()

    def roll_dice(self):
        for i in range(5):
            self.dice[i].roll()

Name = Diceroller()