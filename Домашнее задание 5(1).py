def letter_stat(our_str):
 letters_dict = dict({c : our_str.count(c) for c in our_str})
 return print(letters_dict)
our_str = 'понимание'
letter_stat(our_str)