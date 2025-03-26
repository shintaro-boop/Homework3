print ('введите две строки')
string1 = str(input ("Первая строка = "))
string2 = str(input ("Вторая строка = "))
print (string1.replace (string1[0:2], string2[0:2]), string2.replace (string2[0:2], string1[0:2]))