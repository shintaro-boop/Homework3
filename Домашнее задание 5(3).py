def everything_for_your_cat(cats_data):
    namemaster = str(input('Введите имя хозяина(ки) = '))
    infocat = str(input('Введите кличку котика = '))
    agecat = int(input('Введите востраст котика ='))
    cats_info = [infocat, agecat]
    cats_data.update ({[*cats_info] : namemaster})


    return our_str