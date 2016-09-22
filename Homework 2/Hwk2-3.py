def palindrome_test(phrase):
    phrase = str.lower(phrase)

    # If the inverse of the string is the same as the string itself, the string
    # is a palindrome.

    return phrase == phrase[::-1]


while True:
    word = raw_input("Enter a word to see if it's a palindrome: ")
    print palindrome_test(word)
