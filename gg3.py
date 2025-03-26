string1 = 'Добро пожаловать'
print('Инедкс первой буквы "о" :', string1.find('о', 2,3))
print (string1.replace('Добро', 'Пока'))
print (string1.isdigit(), string1.isalpha(), string1.isalnum(),
       string1.islower(), string1.isupper())
print (string1.startswith('Добро'), string1.endswith('ать'))
print (string1.split('о'))