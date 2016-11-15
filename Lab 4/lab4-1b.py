import random

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
def loop_guesses(correct_num):
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

        if guess_count == 7:
            print "You're out of guesses!"
            print "The number I was thinking of was " + str(correct_num) + "!"
            return 8

        print


# Generate the random number for the game to use
def generate_num():
    random.seed()
    num = random.randint(1, 100)

    return num


# Calculate the user's winnings based on their number of guesses
def calc_winnings(guess_count):
    if guess_count == 8:
        return -10
    if guess_count == 7:
        return 0

    return 8 - guess_count


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
        print "I am thinking of a number between 1 and 100."

        num = generate_num()

        guesses = loop_guesses(num)
        round_winnings = calc_winnings(guesses)
        game_winnings += round_winnings

        show_winnings(round_winnings, game_winnings)

        playing = prompt_repeat()

loop_rounds()
