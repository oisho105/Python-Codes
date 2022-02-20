from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print('its running')

class programmer:
    def work(self):
        print('solve problem')

# com = computer()
com1 = laptop()
# com.process()
com1.process()
