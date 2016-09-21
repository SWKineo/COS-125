def left_pad(string, padder, pad_length):
    while len(string) < pad_length:
        string = padder + string

    return string


phrase = raw_input("Enter a word or number that you want to pad: ")
pad_char = raw_input("What character would you like to pad it with? ")
length = int(raw_input("How long would you like the string to be? "))

print left_pad(phrase, pad_char, length)
