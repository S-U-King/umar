class car:
    def __init__(self, make):
        self.make = make
    def getcar(self):
        print(self.make)

mycar = car('Tesla')
newcar = car('Toyota')


mycar.getcar()
newcar.getcar()

class bike:
    def __init__(self, make):
        self.make = make
    def getbike(self):
        print(self.make)

mybike = bike('Haya bosa')
newbike = bike('Kawasaki ninja')


mybike.getbike()
newbike.getbike()