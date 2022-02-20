
class car:
    def __init__(self):
        self.mil = 10
        self.com = 'BMW'

    wheels = 4

c1 = car()
c2 = car()

c1.mil = 8
car.wheels = 3  # change the class's variable

print(c1.mil, c1.com, c1.wheels)
print(c2.mil, c2.com, c2.wheels)