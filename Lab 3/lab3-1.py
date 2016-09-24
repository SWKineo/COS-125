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

seq_length = int(raw_input("How long would you like your sequences to be? "))
seq_count = int(raw_input("How many sequences would you like? "))
print

list = gen_sequence_list(seq_length, seq_count)

for i in range(len(list)):
    print list[i]
