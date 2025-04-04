def repeats(our_str):
    letters_dict = dict({c: our_str.count(c) for c in our_str})
    new_str = letters_dict
    for key, value in new_str.items() :
        print (f"{key}_{value}", end= '')
    return new_str
our_str = 'понимание'
repeats(our_str)