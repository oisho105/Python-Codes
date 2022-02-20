class A:
    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')

class B(A):     # B is inheriting all features of A
            # B is subclass, A is superclass
    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')

class C(B):     # c is inheriting all features of B &A
    def feature5(self):
        print('feature 5 is working')

b1 = B()
c1 = C()

b1.feature1()
c1.feature3()