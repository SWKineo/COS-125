"""
Created by Spencer Ward
COS 125 Fall 2016
Homework #3
"""

import Tkinter
from random import randint


class Hand:

    # Initialize the Hand with randomly set dice
    def __init__(self, frame):
        self.dice = []
        self.dice_values = []

    # Initializing dice_values and dice in one loop for efficiency
        for i in range(5):
            new_val = randint(1, 6)
            self.dice.append(Die(frame, new_val))
            self.dice_values.append(new_val)

    def roll(self):
        for i in range(5):
            # Using Die's roll method to set generate a random number allows
            # each of the dice to update their own labels
            self.dice_values[i] = self.dice[i].roll()

    # Classifies the Hand as one of the following:
    #     Five of a Kind (29,000+)
    #     Four of a Kind (28,000-28,999)
    #     Full House (Three of a Kind and a Pair) (27,000-27,999)
    #     Three of a Kind (26,000-26,999)
    #     Two Pairs (25,000 - 25,999)
    #     Pair (15,000-24,999)
    #     High Die (0-14,999)
    # Numbers are high to allow implementing scoring priority and to improve
    # readability
    #
    # Returns the classification, along with a score to signify value
    # Scores were never used, but should work for ranking hands in a poker style
    # game.
    def classify(self):
        # Holds exclusive matches (3, 4, and 5)
        major_count = (-1, -1)
        # Holds matches that there can be multiple of (1 and 2)
        pairs = []
        singles = []

        for i in range(1, 7):
            count = self.dice_values.count(i)

            if count > 2:
                major_count = (i, count)
            elif count == 2:
                pairs.append(i)
            elif count == 1:
                singles.append(i)

        if major_count[1] == 5:
            return "Five of a Kind of " + str(major_count[0]), \
                   29000 + 10 * major_count[0]
        elif major_count[1] == 4:
            return "Four of a Kind of " + str(major_count[0]), \
                   28000 + 10 * major_count[0] + singles[0]
        elif major_count[1] == 3:
            if len(pairs) == 1:
                return "Full House of " + str(major_count[0]) + " and " + \
                       str(pairs[0]), 27000 + 10 * major_count[0] + pairs[0]
            else:
                return "Three of a Kind of " + str(major_count[0]), \
                       26000 + 100 * major_count[0] + max(singles)
        elif len(pairs) == 2:
            return "Pairs of " + str(pairs[0]) + "'s and " + str(pairs[1]) + \
                   "'s", 250000 + 100 * max(pairs) + 10 * min(pairs) + singles[0]
        elif len(pairs) == 1:
            singles.sort()
            return "Pair of " + str(pairs[0]), \
                   150000 + 1000 * pairs[0] + 100 * singles[2] + \
                   10 * singles[1] + singles[0]
        else:
            singles.sort()
            # Separates each die into a range. All of the lower die can only add
            # up to 1 below 1 x the number above them. It's over engineered, and
            # still not all that optimized, but I was bored, and it should work.
            return "High Die of " + str(singles[4]), \
                   360 * singles[4] + 60 * singles[3] + \
                    12 * singles[2] + 3 * singles[1] + singles[0]


class Die:
    def __init__(self, frame, init_value=0):
        self.images = [
            Tkinter.PhotoImage(file='1.gif'),
            Tkinter.PhotoImage(file='2.gif'),
            Tkinter.PhotoImage(file='3.gif'),
            Tkinter.PhotoImage(file='4.gif'),
            Tkinter.PhotoImage(file='5.gif'),
            Tkinter.PhotoImage(file='6.gif')
        ]

        if 0 < init_value < 6:
            self.value = init_value
        else:
            self.value = randint(1, 6)

        self.display = Tkinter.Label(frame,
                                     image=self.images[self.value - 1],
                                     relief='flat',
                                     borderwidth=5,
                                     bg='white')
        self.display.pack(side='left')

    def set_value(self, value):
        self.value = value

    def roll(self):
        self.value = randint(1, 6)
        self.display.config(image=self.images[self.value - 1])

        return self.value


class DicePoker:
    def __init__(self):
        dice_win = Tkinter.Tk()
        dice_win.title("Roll 'Em Up")
        dice_win.minsize(width=465, height=100)
        dice_win.config(bg='white')

        hand_frame = Tkinter.Frame(dice_win)
        self.hand = Hand(hand_frame)

        separator_top = Tkinter.Frame(height=2, bd=1, relief='sunken')

        self.classification = Tkinter.Label(dice_win,
                                       text=self.hand.classify()[0],
                                       font=('Arial', 15),
                                       foreground='#20233a',
                                       bg='white')

        separator_bottom = Tkinter.Frame(height=2, bd =1, relief='sunken')

        roll_button = Tkinter.Button(dice_win,
                                     text='Roll the Dice',
                                     command=self.roll,
                                     font=('Arial', 20),
                                     foreground='#20233a',
                                     activeforeground='#2b3166',
                                     bg='#f7f7f7',
                                     relief='ridge',
                                     borderwidth=1,
                                     width=10)

        hand_frame.pack(pady=5)
        separator_top.pack(fill='x', padx=5, pady=5)
        self.classification.pack()
        separator_bottom.pack(fill='x', padx=5, pady=5)
        roll_button.pack(side='bottom', pady=5)
        dice_win.mainloop()

    def roll(self):
        self.hand.roll()
        self.classification.config(text=self.hand.classify()[0])


varName = DicePoker()


def classify(self):
    # Holds exclusive matches (3, 4, and 5)
    major_count = (-1, -1)
    # Holds pairs
    pairs = []
    # Holds die with no matches
    singles = []

    for i in range(1, 7):
        count = self.dice_values.count(i)

        if count > 2:
            major_count = (i, count)
        elif count == 2:
            pairs.append(i)
        elif count == 1:
            singles.append(i)

    if major_count[1] == 5:
        return "Five of a Kind"
    elif major_count[1] == 4:
        return "Four of a Kind"
    elif major_count[1] == 3:
        if len(pairs) == 1:
            return "Full House"
        else:
            return "Three of a Kind"
    elif len(pairs) == 2:
        return "Pairs"
    elif len(pairs) == 1:
        return "Pair"
    else:
        return "High Die"
