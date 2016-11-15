"""
Created by Spencer Ward
COS 125 Fal 2016
Lab #5
"""

import Tkinter
from random import randint


class Die:
    def __init__(self, frame):
        self.value = randint(1, 6)
        self.display = Tkinter.Label(frame,
                                     text=str(self.value),
                                     font=('Arial', 30),
                                     relief='ridge',
                                     borderwidth=5,
                                     bg='white')
        self.display.pack(side='left')

    def roll(self):
        self.value = randint(1, 6)
        self.display.config(text=str(self.value))


class DiceRoller:
    def __init__(self):
        dice_win = Tkinter.Tk()
        dice_win.title('Roll the Dice')

        dice_frame = Tkinter.Frame(dice_win)
        self.dice = []
        for i in range(3):
            self.dice.append(Die(dice_frame))

        roll_button = Tkinter.Button(dice_win,
                                     text='Roll Again',
                                     command=self.roll_dice,
                                     font=('Arial', 30),
                                     relief='raised',
                                     borderwidth=6,
                                     width=10)

        dice_frame.pack()
        roll_button.pack(side='bottom')
        dice_win.mainloop()

    def roll_dice(self):
        for i in range(3):
            self.dice[i].roll()


varName = DiceRoller()
