def bottle_verse_special(verse_number):
    if verse_number == 2:
        print "Two bottles of beer on the wall, two bottles of beer."
        print "Take one down and pass it around, one bottle of beer on the wall."
    elif verse_number == 1:
        print "One bottle of beer on the wall, one bottle of beer."
        print "Take one down and pass it around, no more bottles of beer on the wall."
    elif verse_number == 0:
        print "No more bottles of beer on the wall, no more bottles of beer."
        print "Go to the store and buy some more, ninety-nine bottles of beer on the " \
              "wall."


# Converts numbers to their English form by setting and adding the variables
# tens_string, hyphen_string, ones_string
def convert_to_word(num, uppercase):
    tens_place_lower = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
                        "seventy", "eighty", "ninety"]
    tens_place_upper = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                        "Seventy", "Eighty", "Ninety"]
    ones_place_lower = ["", "one", "two", "three", "four", "five", "six",
                        "seven", "eight", "nine", "ten", "eleven",
                        "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                        "seventeen", "eighteen", "nineteen"]
    ones_place_upper = ["", "One", "Two", "Three", "Four", "Five", "Six",
                        "Seven", "Eight", "Nine", "Ten", "Eleven",
                        "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                        "Seventeen", "Eighteen", "Nineteen"]

    tens_string = ""
    hyphen_string = ""

    if num < 19:

        if uppercase:
            ones_string = ones_place_upper[num]
        else:
            ones_string = ones_place_lower[num]
    else:
        if uppercase:
            tens_string = tens_place_upper[num / 10]
        else:
            tens_string = tens_place_lower[num / 10]

        ones_value = num % 10
        ones_string = ones_place_lower[ones_value]

        if ones_value != 0:
            hyphen_string = "-"

    return tens_string + hyphen_string + ones_string


def bottle_verse(verse_number):
    if verse_number > 2:
        print convert_to_word(verse_number, True) + " bottles of beer on the wall, " \
              + convert_to_word(verse_number, False) + " bottles of beer."
        print "Take one down and pass it around, " + \
              convert_to_word(verse_number - 1, False) + " bottles of beer on the wall."
    else:
        bottle_verse_special(verse_number)


for i in range(99, -1, -1):
    bottle_verse(i)
    print
