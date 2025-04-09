class Trigon  :
    def __init__(self, *storona : int ) :
        self.storona = storona
    def printtrigon (self):
        try :
            for i in self.storona :
                if len(self.storona) > 3 or len(self.storona) < 3 :
                    raise IndexError
                elif i <= 0 :
                    raise ValueError
                elif isinstance(i, int) == False :
                    raise TypeError
                elif self.storona[0] + self.storona[1] <= self.storona[2] or self.storona[1] + self.storona[2] <= self.storona[0] or self.storona[2] + self.storona[0] <= self.storona[1] :
                    raise Exception
            print('Все успешно')
        except IndexError :
            print(f"Передано {len(self.storona)} аргументов, а ожидается 3")
        except ValueError :
            print('Стороны должны быть положительными')
        except TypeError :
            print ('Стороны должны быть числами')
        except Exception :
            print('Не треугольник')
vvod1 = []
for vvod in range(999) :
    try :
        vvod = int(input(f'введите x {vvod + 1} = '))
        vvod1.append(vvod)
    except ValueError :
        break
print (vvod1)
vvod2 =tuple(list(vvod1))
print (vvod2)
c = Trigon (vvod2)
c.printtrigon()