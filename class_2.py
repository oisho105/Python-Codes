
class computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu      # 'cpu', 'ram', these arguments
        self.ram = ram

    def config(self):       # this's called method
        print('config is:', self.cpu, self.ram)

com1 = computer('i5',16)
com2 = computer('ry',8)

com1.config()
com2.config()
