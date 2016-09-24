def seqzip(seq1, seq2):
    master_list = []

    min_length = len(min(seq1, seq2))

    for i in range(min_length):
        master_list.append([seq1[i], seq2[i]])

    return master_list


list = [1, 2, 3, 4, "Hello World", ["one", 1], ("tuple", 3)]
tup = ('a', 'b', 'c', 'd', "Hey World", ["two", 2], ("Tuple", 4), "N/A")

print "List: " + str(list)
print "Tuple: " + str(tup)

print "seqzip(List, Tuple) = " + str(seqzip(list, tup))
