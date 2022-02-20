
class student:
    school = 'Telusko'      # class variable

    def __init__(self,m1,m2,m3):    # 'self' used for instance methods
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
                # defining the var's as function argument

    def avg(self):
        self.x = (self.m1 + self.m2+ self.m3)/3
        return self.x

    def get_m1(self):
        return self.m1  # accessor method

    def set_m1(self):
        return self.m1  # mutator method

    @classmethod      # decorator, needed to define Class Method
    def getschool(cls):     # use 'class' class methods
        return cls.school

    @staticmethod
    def info():     # static method, no 'self', no 'cls'
        print('This is student class')


s1 = student(34,65,71)
s2 = student(89,45,61)

print(s1.avg()); print(s2.avg())    # printing objects
print(student.getschool())          # printing class
print(student.info())