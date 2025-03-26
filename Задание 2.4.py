import os
name = str(input ('Введите пусть к файлу'))
c = os.path.splitext(os.path.basename(name))[0]
print (c)