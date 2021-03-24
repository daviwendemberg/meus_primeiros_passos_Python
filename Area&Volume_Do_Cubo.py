class cubo(object):
    def __init__(self, cubo):
        self.cubo = cubo
    def area(self):
        return self.cubo ** 2
    def volume(self):
        return self.cubo ** 2 * 6

c = cubo(4)

print(f'A area do cubo é:{c.area()}\nE o seu volume é:{c.volume()} ')