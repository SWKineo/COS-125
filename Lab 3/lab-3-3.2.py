def seqzip(seq1, seq2):
    master_list = []

    min_length = len(min(seq1, seq2))

    for i in range(min_length):
        master_list.append([seq1[i], seq2[i]])

    return master_list


# Tests inputs of different lengths and types
print "seqzip([1, 2, 3], 'abcd'"
print seqzip([1, 2, 3], 'abcd')

# Tests inputs of different lengths and types when one list is empty
print "seqzip([], (1, 2))"
print seqzip([], (1, 2))

raw_input("Type anything to continue. ")

# Tests inputs of non-list types (crashes)
print "seqzip(1, [])"
print seqzip(1, [])
