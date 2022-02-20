
class student:
    def __init__(self,name,roll):
        self.name = name; self.roll = roll  # defining arguments
        self.lap = self.laptop()    # defining inner-class

    def show(self):
        print(self.name, self.roll)
        self.lap.show()     # calls 'lap' (so, 'laptop' class) show() method

    class laptop:   # inner class
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'; self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)

s1 = student('Navin',2)
s2 = student('Jenny',3)

s1.show()       # calls 'show()' method of object s1
# print(s1.lap.brand)   # prints brand name

# lap1 = s1.lap   # assigns in 'lap1' var' 's1.lap' var'
# lap2 = s2.lap
