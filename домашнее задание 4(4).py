def multiplication_chain(num):
    count_multy = []
    for element in num :
        w = 0
        while element // 10 != 0 :
            a = element // 10
            b = element % 10
            c = a * b
            w += 1
            if element // 10 == 0 :
                break
            count_multy.appende (w)
    return count_multy