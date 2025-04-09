c = str(input('Язык програмирования = '))
languages = ["C", "C++", "Python", "Java", "Go"]
position = None
for i, element in enumerate(languages):
     if element == c:
         position = i + 1
         break
if position is None:
     print("Элемент не найден.")
else:
     print("Элемент находится на позиции:", position)