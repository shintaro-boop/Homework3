import math
from selectors import SelectSelector

print ('Введите сторону квадрата')
x = float(input("x = "))
p = x+x+x+x
s = x*x
d = x*math.sqrt(2)
print (f'Периметр квадрата равен {p}')
print ('Площадь квадрата равен %s' % (s))
print (round(d,2))


print ('Введите коэффициенты для уравнения\n' 'ax^2+bx+c=0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

discr = b ** 2 - 4 * a* c

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
print ('D = %.2f' % (discr))
print ('x1 = %.2f\n x2 = %.2f' % (x1,x2))
elif discr = 0:
x = (-b) / (2 * a)
print ('D = 0')
print ('x = %.2f' % (x))
else :
print ('Нельзя извлечь корень из отрицательного числа, корней нет')

