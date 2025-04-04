cats_data = {('Мурзик', 5) : 'Вадим', ('Алиса', 3) : 'Вадим' }
def everything_for_your_cat() :
    namemaster = str(input('Введите имя хозяина(ки) = '))
    infocat = str(input('Введите кличку котика = '))
    agecat = int(input('Введите востраст котика = '))
    cats_info = infocat, agecat
    cats_data.update({cats_info : namemaster})
    for key, value in cats_data.keys() :
        if value == namemaster :
            print (f"{key} ", end= '')

        return 
everything_for_your_cat()