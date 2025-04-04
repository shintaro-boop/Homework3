class klass:
    def __init__(self, *value : int ):
        self.value = value
    def segmet (self) :
        try :
            c = []
            for i in self.value :
                for b in i :
                    c.append(b)
                total = sum (c)
            print(total)
        except Exception as ochipka:
            ochipka1= str(ochipka)[::-1]
            print (f'{str(ochipka1)}')
w = klass ((2,2),(9,3))
w.segmet()