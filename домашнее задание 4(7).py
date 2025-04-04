def move_zeros(lst):
    c = lst.count(0)
    while c == 0 :
        for item in lst :
            if item == 0 :
                lst.remove (0)
                lst.append (0)
                c -= 1
        else :
            continue
    return lst