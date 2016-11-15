def leftPad(string, padder, length):
    if len(str(string)) < (length*(str(length))):
        print padder * (length - len(str(string))) + str(string)
    else:
        print

phrase = raw_input("Enter a word or number that you want to pad: ")
pad_char = raw_input("What character would you like to pad it with? ")
length = int(raw_input("How long would you like the string to be? "))

print leftPad(phrase, pad_char, length)