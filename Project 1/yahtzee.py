# Version 1
import random
from time import sleep


class Player:
    round = 1
    max_rounds = 10

    def count_vals(self):
        counter = [0, 0, 0, 0, 0, 0]

        for n in self.dice.dice_list:
            counter[n - 1] += 1

        return counter

    def sum_vals(self):
        sum = 0
        for n in self.dice.dice_list:
            sum += n

        return sum

    def basic_scores(self, score_number):
        score = 0

        for n in self.dice.dice_list:
            if n == score_number:
                score += n
        self.scores[score_number - 1] = score
        return score

    def toak(self):
        counter = self.count_vals()

        for i in range(6):
            if counter[i] >= 3:
                self.scores[6] = self.sum_vals()
                return self.sum_vals()
        return 0

    def foak(self):
        counter = self.count_vals()

        for i in range(6):
            if counter[i] >= 4:
                self.scores[7] = self.sum_vals()
                return self.sum_vals()
        return 0

    def fh(self):
        counter = self.count_vals()

        triple = False
        double = False

        for n in counter:
            if n == 3:
                triple = True
            elif n == 2:
                double = True

        if triple and double:
            self.scores[8] = 25
            return 25
        return 0

    def ss(self):
        counter = self.count_vals()
        count = 0

        for n in counter:
            if n > 0:
                count += 1
            if count >= 4:
                self.scores[9] = 30
                return 30
            if n == 0:
                count = 0

        return 0

    def ls(self):
        counter = self.count_vals()
        count = 0

        for n in counter:
            if n > 0:
                count += 1
            if count >= 5:
                self.scores[10] = 40
                return 40
            if n == 0:
                count = 0

        return 0

    def ya(self):
        # self.score_options[11] = ""
        val = self.dice.dice_list[0]

        for n in self.dice.dice_list[1:]:
            if n != val:
                self.scores[11] = 50
                return 50

        return 0

    def ch(self):

        self.scores[12] = self.sum_vals()
        return self.sum_vals()

    def __init__(self, name):
        self.name = name

        self.scores = []

        self.dice = Dice()

        for i in range(13):
            self.scores.append(0)

        self.scoring = {
            'threeofakin': self.toak,
            'fourofakin': self.foak,
            'fullhouse': self.fh,
            'smallstraight': self.ss,
            'largestraight': self.ls,
            'yahtzee': self.ya,
            'chance': self.ch
        }

        self.score_options = {
            'aces': 'Aces',
            'twos': 'Twos',
            'threes': 'Threes',
            'fours': 'Fours',
            'fives': 'Fives',
            'sixes': 'Sixes',
            'sevens': 'Sevens',
            'threeofakin': 'Three-Of-A-Kind',
            'fourofakin': 'Four-Of-A-Kind',
            'fullhouse': 'Full House',
            'smallstraight': 'Small Straight',
            'largestraight': 'Large Straight',
            'yahtzee': 'Yahtzee',
            'chance': 'Chance'
        }

    def print_options(self):
        line_length = 25

        key_list = self.score_options.keys()

        print "Your scoring options are",
        for i in range(len(key_list)):
            stype = self.score_options[key_list[i]]

            if line_length + len(stype) > 80:
                print
                line_length = 0

            line_length += len(stype)

            if i == len(key_list) - 1:
                comma = "."
            else:
                comma = ","

            print stype + comma,

    def score(self, score):
        try:
            self.score_options.pop(score.lower())
        except KeyError:
            print "You can't use that scoring type!\n"
            return False

        try:
            upper = {
                "aces": 1,
                "twos": 2,
                "threes": 3,
                "fours": 4,
                "fives": 5,
                "sixes": 6
            }

            print "You have earned " + \
                  str(self.basic_scores(upper[score.lower()])) + " points!"
            sleep(1)
        except KeyError:
            try:
                print "You have earned " + \
                      str(self.scoring[score.lower()]()) + " points!"
                sleep(1)
            except KeyError:
                print "That is not a valid scoring type!\n"
                return False


        return True

    def player_total(self):
        total = 0

        for n in self.scores:
            total += n

        return total


class Dice:

    def __init__(self):
        random.seed()

        self.dice_list = []

        self.queue_roll = []

        for i in range(5):
            self.dice_list.append('-')

        self.rolls_left = 3
        self.rolling = False

    def roll(self):
        for n in self.queue_roll:
            self.dice_list[n - 1] = random.randint(1, 6)

        self.rolls_left -= 1

    def clear(self, selection=(1, 2, 3, 4, 5)):
        for n in selection:
            self.dice_list[n - 1] = '-'
        self.rolling = True

    def display_dice(self):
        print " ---        " * 5

        for d in self.dice_list:
            print "| " + str(d) + " |      ",

        print
        print " ---        " * 5


def clear_screen():
    # # Operating system type; nt for Windows, posix for Unix
    # if os.name == 'nt':
    #     os.system("cls")
    # elif os.name == 'posix':
    #     os.system("clear")
    # else:

    print 80 * '\n'


def parse_term(string):
    args = [""]
    arg = 0

    # Keeps track of whether the last character was a spacer
    new_spacer = True

    for c in string:
        if c == " " or c == "," or c == "D" or c == 'd' or c == '-':
            if new_spacer:
                args.append("")
                new_spacer = False
                arg += 1
        else:
            args[arg] += c
            new_spacer = True

    return args


def handle_input(user_input, players, p):
    args = parse_term(user_input)

    if args[0].lower() == "roll":
        if players[p].dice.rolls_left == 0:
            print "You are out of rolls!\n"
            return True, players, p

        if len(args) > 1:
            selection = []
            for n in args[1:]:
                try:
                    selection.append(int(n))
                except ValueError:
                    print "Please enter your dice selection in digits"
                    sleep(1.3)
                    return True, players, p
        else:
            selection = [1, 2, 3, 4, 5]
        players[p].dice.queue_roll = selection
        players[p].dice.clear(selection)
        return False, players, p
    elif args[0].lower() == "score":
        # Reconstruct arguments as one phrase

        if len(args) < 2:
            print "Please enter a scoring type.\n"
            return True, players, p

        for n in args[2:]:
            args[1] += n

        success = players[p].score(args[1])

        if success:
            players[p].dice.clear()
            players[p].dice.rolls_left = 3
            p += 1

            if p == len(players):
                p -= len(players)
                Player.round += 1

        return not success, players, p
    else:
        print "That's not a valid command!\n"
        return True, players, p


def update_output(players):
    # Player number
    p = 0

    while Player.round <= Player.max_rounds:
        clear_screen()
        for i in range(len(players)):
            if i == p:
                print "**" + players[i].name + "**:",
            else:
                print players[i].name + ":",

            print players[i].player_total()

        print "\nRound:", Player.round

        print "\n\n"

        players[p].dice.display_dice()

        print "\n\n"

        waiting = True

        while waiting:
            print players[p].name + ":"
            if players[p].dice.rolls_left > 0:
                print "Type 'roll' to roll, or type 'roll D1, D5' to"
                print "roll certain dice, in this case 1 and 5."
            print "You have " + str(players[p].dice.rolls_left) + " rolls left."

            print "\nWhen you're ready to score, type 'score <option>'"
            players[p].print_options()

            # Exits the loop if the input was acceptable
            if players[p].dice.rolling:
                sleep(0.5)
                players[p].dice.rolling = False
                players[p].dice.roll()
                waiting = False
            else:
                waiting, players, p = handle_input(
                    raw_input("\n"),
                    players,
                    p
                )
                if waiting:
                    sleep(1)

    highest = -1
    highest_name = "Nobody"
    for pl in players:
        if pl.player_total() > highest:
            highest = pl.player_total()
            highest_name = pl.name
    print highest_name, "wins!"


def protected_input(prompt):
    try:
        return int(raw_input(prompt))
    except ValueError:
        print "I'm sorry, what was that?\n"
        return protected_input(prompt)


def main():
    rounds = protected_input("How many rounds would you like to play? ")
    player_count = protected_input("How many players would you like? ")

    players = []

    for i in range(player_count):
        name = raw_input("Player " + str(i + 1) + ", what is your name? ")
        players.append(Player(name))

    Player.max_rounds = rounds

    update_output(players)


if __name__ == "__main__":
    main()