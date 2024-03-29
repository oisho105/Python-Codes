class A:
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')

class B:
    def __init__(self):
        # super().__init__()  # calls the init of its superclass
        print('in B init')

    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')

class C(B,A):           # order change (A,B)
    def __init__(self):
        super().__init__()
        print('in C init')

    def feat(self):
        super().feature2()

a1 = C()
a1.feat()
