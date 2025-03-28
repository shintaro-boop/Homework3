num = [1,2,3,4,5,6]
def sum_digits(num):
    our_sum = []
    for element in num :
        c = num // 10
        b = num % 10
        a = b + c
        our_sum.append (a)
    return our_sum