import random

while True:
    wins = 0

    ynr = raw_input('Do you want to swap curtains' +
                    '? (y/n/r) ')

    for i in range(1000):
        choices = ['1', '2', '3']
        car = random.choice(choices)
        # human = raw_input('Please select curtain 1, 2 or 3. ')
        human = random.choice(choices)

        choices.remove(car)
        if human in choices:
            choices.remove(human)

        empty = random.choice(choices)

        # print "The empty curtain is",empty

        choices = ['1', '2', '3']
        choices.remove(empty)
        choices.remove(human)

        if ynr == 'r':
            yn = random.choice(['y', 'n'])
        else:
            yn = ynr

        if yn == 'y':
            human = choices[0]

        if human == car:
            # print 'Congratulations! You won the prize.'
            wins += 1
            # else:
            # print 'Sorry! You did not win the prize. ',
            # print 'It was behind curtain '+car+'.'

    print wins, "/ 1000 Wins"
