def palindrome(phrase):
    phrase = str.lower(phrase)

    length = len(phrase)

    half1 = ""
    half2 = ""

    # Range is (length - 1) / 2 so that the function always rounds down to the
    # index of the character before the middle of the word.
    for i in range((length - 1) / 2):
        half1 += phrase[i]

    for i in range(length - 1, length / 2, -1):
        half2 += phrase[i]

    return half1 == half2


while (True):
    word = raw_input("Enter a word to see if it's a palindrome: ")
    print palindrome(word)
