import random
a = 1
c = int(input('Давайте сыграем в игру. Вам нужно ввести число от 1 до 10 и угадать какое число загадал я. Начинаем) Ваше число = '))
while c > 10:
    print ('Мы же договорились от 1 до 10)')
    c = int(input('Я жду ) = '))
    if c <= 10:
        continue
while a != c :
    a = random.randint(1, 10)
    c = int(input('Попробуем еще раз = '))
    if c > 10:
        print ('Мы же договорились от 1 до 10)')
    elif  a == c :
        print ('Поздравляем ты победил ты сломал ее(')
    else :
        continue