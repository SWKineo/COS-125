import random


def gen_sequence(length):
    seq = ""

    for i in range(length):
        seq += str(random.randint(0, 9))

    return seq


def gen_sequence_list(length, count):
    list = []

    for i in range(count):
        list.append(gen_sequence(length))

    return list


random.seed()

# Checks the function's behavior when given a length of 0
print "gen_sequence_list(0, 2)"
print gen_sequence_list(0, 2)

# Checks the function's behavior when given a count of 0
print "gen_sequence_list(2, 0)"
print gen_sequence_list(2, 0)

# Checks the function's behavior when given a length and a count of 0
print "gen_sequence_list(0, 0)"
print gen_sequence_list(0, 0)

# Checks the function's handling of larger numbers
print "gen_sequence_list(15, 3)"
print gen_sequence_list(15, 3)

# Checks the functions handling of negative numbers
print "gen_sequence_list(-1, 5)"
print gen_sequence_list(-1, 5)

print "gen_sequence_list(5, -1)"
print gen_sequence_list(5, -1)

# Waits before running code that will crash the program
raw_input("Type anything to continue. ")

# Checks the function's handling of floats (crashes)
print "gen_sequence_list(5.0, 1.0)"
print gen_sequence_list(5.0, 1.0)

# Checks the function's handling of strings (crashes)
print "gen_sequence_list(1, '5')"
print gen_sequence_list(1, '5')
