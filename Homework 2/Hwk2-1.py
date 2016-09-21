def bottle_verse_special(verse_number):
    if verse_number == 2:
        print "2 bottles of beer on the wall, 2 bottles of beer."
        print "Take one down and pass it around, 1 bottle of beer on the wall."
    elif verse_number == 1:
        print "1 bottle of beer on the wall, 1 bottle of beer."
        print "Take one down and pass it around, no more bottles of beer on the wall."
    elif verse_number == 0:
        print "No more bottles of beer on the wall, no more bottles of beer."
        print "Go to the store and buy some more, 99 bottles of beer on the wall."


def bottle_verse(verse_number):
    if verse_number > 2:
        print verse_number, "bottles of beer on the wall,", verse_number, \
            "bottles of beer."
        print "Take one down and pass it around,", verse_number - 1, "bottles of " \
              "beer on the wall."
    else:
        bottle_verse_special(verse_number)

for i in range(99, -1, -1):
    bottle_verse(i)
    print
