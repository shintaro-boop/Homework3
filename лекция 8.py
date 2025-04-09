try:
    a = input("Введите первое число: ")
    b = input("Введите второе число: ")
    result = int(a) / int(b)
    print("Результат: ", result)
    print('Операция деления выполнена успешно!')
except ZeroDivisionError:
    print("Нельзя делить на ноль!")
else:
    print("Результат в квадрате: ", result**2)
