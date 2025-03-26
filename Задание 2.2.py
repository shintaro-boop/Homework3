import math
print ('Введите коэффициенты для уравнения\n' 'ax^2+bx+c=0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discr = b ** 2 - 4 * a* c

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print ('D = %.2f' % discr)
    print ('x1 = %.2f\n x2 = %.2f' % (x1, x2))
elif discr == 0:
    x = (-b) / (2 * a)
    print ('D = 0')
    print ('x = %.2f' % x)
else :
    print ('Нельзя извлечь корень из отрицательного числа, корней нет')