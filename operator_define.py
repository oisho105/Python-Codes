
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):       # defines + operator
        p1 = self.m1 + other.m1     # defines operation 1
        p2 = self.m2 + other.m2     # defines operation 2
        sum = student(p1,p2)        # defining an object/func
        return sum              # returns that object

    def __gt__(self,other):         # defines > operator
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return self.m1, self.m2

s1 = student(58,70)
s2 = student(60,65)

s3 = s1 + s2    # defining object s3
print(s3.m1, end=' '); print(s3.m2)
"""
if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')    """

print(s1.__str__())