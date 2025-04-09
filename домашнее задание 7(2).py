class PersonInfo :

    def __init__ (self, name : str , age : int , *rabota) :
        self.name = name
        self.age = age
        self.rabota = rabota
    def shortname (self) :
        print (f'Имя сотрудника : {self.name}')
    def path_deps (self) :
        for i in self.rabota  :
            print (f'{i} --> ', end = '')
    def new_salary (self) :
        bukvi = ''.join(self.rabota)
        bukvi1 = list(bukvi)
        letters_dict = dict({c: bukvi1.count(c) for c in bukvi1})
        summa = sorted(letters_dict.values(),reverse=True)
        summakonec = summa[0]+summa[1]+summa[2]
        konec = 1337*self.age*summakonec
        print (konec)
c = PersonInfo('Александр Шленский', 32, 'Разработка', 'УК', 'Автотесты')
c.shortname()
c.new_salary()
c.path_deps()
