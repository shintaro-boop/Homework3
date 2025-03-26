string1 = 'wtf'
string2 = str(input('Введите строку содержащую w, t, f '))
a = string2.find ('w')
b = string2.find ('t')
c = string2.find ('f')
d = min(a,b,c)
w = max (a,b,c)
print (string2[d:w+1])