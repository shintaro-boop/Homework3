def which_triangle(a, b, c):
    type_triangle = []
    if a + b >= c or b + c >= a or a + c >= b :
        type_triangle.append('Не треугольник')
    elif a==b or c==b or a==c :
        type_triangle.append('Равнобедренный')
    elif a==b==c :
        type_triangle.append('Равносторонний')
    else :
        type_triangle.append('Обычный')
    return type_triangle
