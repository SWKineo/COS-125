def left_pad(string, padder, pad_length):
    string = str(string)

    while len(string) < pad_length:
        string = padder + string

    return string

def draw_grid():
    print "ASCII TABLE".center(86, " ")
    print "-----+---0---+---1---+---2---+---3---+---4---+---5---+---6---+---7" \
          "---+---8---+---9---+"

    for i in range(13):
        print left_pad(i, " ", 4) + " |",

        for n in range(10):
            char_num = i * 10 + n

            if char_num < 32:
                char = "ctrl"
            elif char_num == 127:
                char = "DEL"
            elif char_num > 127:
                char = "n/a"
            else:
                char = chr(char_num)

            print char.center(5, " ") + " |",

        print
        print "-----+-------+-------+-------+-------+-------+-------+-------+" \
              "-------+-------+-------+"

draw_grid()