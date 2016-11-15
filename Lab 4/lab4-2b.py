import random


# Generates a random number between 1 and 100,000
def generate_num():
    random.seed()
    num = random.randint(1, 100000)

    return num


# Finds the number of guesses allowed for the given range
def get_range(num):
    if num < 101:
        return (1, 100)
    if num < 1001:
        return (101, 1000)
    if num < 15001:
        return (1001, 15000)
    else:
        return (15001, 100000)


# Finds the number of guesses allowed for the given range
def get_guess_count(range_num):
    if range_num[0] == 1:
        return 7
    if range_num[0] == 101:
        return 10
    if range_num[0] == 1001:
        return 14
    if range_num[0] == 15001:
        return 17


# Finds the penalty for failing to guess within the limit
def get_penalty(guess_max):
    return -2 * guess_max


# Finds the reward for a certain number of guesses given the guess limit
def get_reward(guess_max, guess_count):
    if guess_count == guess_max + 1:
        return get_penalty(guess_max)
    if guess_count == guess_max:
        return 0

    return guess_max - guess_count + 1


# Displays the number range and betting rules to the user
def show_rules(range_num, guess_max, win_total):
    print "I am thinking of a number between", range_num[0], "and", range_num[1]

    print "You have", guess_max, "guesses allowed."
    print "You have $" + str(win_total) + " right now."
    print "If you take too many guesses, you will lose $" + \
        str(abs(get_penalty(guess_max))) + "."
    print "If you take fewer than that, you will receive a reward:"
    for i in range(1, 4):
        print str(i) + "   $" + str(get_reward(guess_max, i))

    print "..."
    print str(guess_max - 1) + "   $2"
    print str(guess_max) + "   $0"


# Prompt the user for their guess
def prompt_guess():
    num_raw = raw_input("Can you guess what number I'm thinking of? ")

    return int(num_raw)


# Check the user's guess against the game's number
# -1 is too low
#  0 is the correct number
#  1 is too high
def check_guess(guess, correct_num):
    if guess == correct_num:
        return 0
    elif guess < correct_num:
        return -1
    elif guess > correct_num:
        return 1


# Prompt the user for a guess and loop until their guess is correct
# Returns number of how many guesses the user needed
def loop_guesses(correct_num, guess_max):
    guess = -1
    guess_count = 0

    while guess != correct_num:
        guess = prompt_guess()
        guess_count += 1

        guess_status = check_guess(guess, correct_num)

        if guess_status == 0:
            print "Your guess was correct!"
            print "You guessed the number in", guess_count, "guesses!"

            return guess_count

        elif guess_status == -1:
            print "Your guess was too low. Try again!"
        else:
            print "Your guess was too high. Try again!"

        if guess_count == guess_max:
            print "You're out of guesses!"
            print "The number I was thinking of was " + str(correct_num) + "!"
            return guess_max + 1

        print


# Calculate the user's winnings based on their number of guesses
def calc_winnings(guess_count, guess_max):
    if guess_count == guess_max + 1:
        return -10
    if guess_count == guess_max:
        return 0

    return guess_max - guess_count + 1


# Display the user's winnings for the round, along with their total winnings
def show_winnings(win_round, win_total):
    if win_round >= 0:
        print "You won $" + str(win_round) + " this round"
    else:
        print "You have lost $" + str(abs(win_round)) + " this round"

    if win_total > 0:
        print "You have $" + str(win_total) + " so far"
    else:
        print "You have -$" + str(abs(win_total)) + " so far"

    print


# Prompts the user to ask them if they want to go to the next round
def prompt_repeat():
    prompt = raw_input("Would you like to play another round (y/n)? ")

    prompt = prompt.lower()

    if prompt == 'y' or prompt == 'yes':
        return True
    elif prompt == 'n' or prompt == 'no':
        return False
    else:
        "I'm sorry, I don't know what you're saying."
        print
        return prompt_repeat()


# Loop through each of the game rounds, stopping when the user decides to exit
def loop_rounds():
    playing = True
    game_winnings = 0

    while playing:

        num = generate_num()
        range_num = get_range(num)
        guess_max = get_guess_count(range_num)

        show_rules(range_num, guess_max, game_winnings)

        guesses = loop_guesses(num, range_num, guess_max)
        round_winnings = calc_winnings(guesses, guess_max)
        game_winnings += round_winnings

        show_winnings(round_winnings, game_winnings)

        playing = prompt_repeat()

loop_rounds()
