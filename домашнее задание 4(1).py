def which_triangle(a, b, c):
    type_triangle = []
    if a + b <= c or b + c <= a or a + c <= b :
        type_triangle.append('Не треугольник')
    elif a==b==c  :
        type_triangle.append('Равносторонний')
    elif a==b or a==c or b==c :
        type_triangle.append('Равнобедренный')
    else :
        type_triangle.append('Обычный')
    return print(type_triangle)
a = int(input('Введите сторону а треугольника = '))
b = int(input('Введите сторону b треугольника = '))
c = int(input('Введите сторону c треугольника = '))
which_triangle(a,b,c)