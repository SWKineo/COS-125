# Generates a random number between 1 and 100,000
def gen_number():
    return 15656


# Returns the minimum value in the range given the generated number
def get_range(num):
    return 15001


# Finds the number of guesses allowed for the given range
def get_guess_count(range):
    return 17


# Finds the penalty for failing to guess within the limit
def get_penalty(guess_max):
    return 24


# Finds the reward for a certain number of guesses given the guess limit
def get_reward(guess_max, guess_count):
    return 15


# Displays the number range and betting rules to the user
def show_rules(range, guess_max):
    return
