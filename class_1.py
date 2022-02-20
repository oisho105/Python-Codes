
class computer:
    def config(self):       # this's called method
        print('i5, 16gb, 11B')

com1 = computer()   # 'com1' object, asumes class 'computer'
com2 = computer()   # 'com2' object, belongs to class 'computer'

com1.config()
com2.config()

# print(com1)   # prints the address