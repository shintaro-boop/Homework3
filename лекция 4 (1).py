my_age = int(input('Введите возраст '))
if my_age < 18 :
    print ('Ура еще не работаю')
elif my_age > 70 :
    print('Мама я пенсионер')
else :
    print ('Ой ой пора на работу')



a = int(input('Введите переменную а '))
b = int(input('Введите переменную b '))
rez = a + b if a > b else a - b
print ('Ваш итог =', rez)