
class segment :
    def __init__(self, x1 : float, x2 : float, y1 : float, y2 : float):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def kakyadlina (self) :
        dlina = ((self.x1-self.x2)**2 + (self.y1-self.y2)**2)**0.5
        print (f'Длина вектора = {dlina}')
    def x_axis_intersection (self) :
        if self.x1 > 0 and self.x2 < 0 or self.x1 < 0 and self.x2 > 0 :
            print ('True')
        else :
            print ('False')
    def y_axis_intersection(self):
        if self.y1 > 0 and self.y2 < 0 or self.y1 < 0 and self.y2 > 0:
            print('True')
        else:
            print('False')
c = segment(-2,5,-7,9)
c.kakyadlina()
c.x_axis_intersection()
c.y_axis_intersection()

