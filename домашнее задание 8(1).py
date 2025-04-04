def treatment_sum (our_turple) :
    try :
        w = len(our_turple)
        if w > 2 :
            raise ZeroDivisionError
        c = sum(our_turple)
        print(f'Сумма = {c}')
    except (ValueError, TypeError):
        print ('Нельзя сложить эти данные')
    except NameError:
            print ('Недостаточно данных')
    except ZeroDivisionError:
            print('Много данных')
x1 = (input(f'Введите данные x1 = '))
x2 = (input(f'Введите данные x2 = '))
our_turple = (x1, x2)
treatment_sum(our_turple)