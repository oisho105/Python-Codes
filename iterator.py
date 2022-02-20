
class topten:
    def __init__(self):
       self.num = 1

    def __iter__(self):     # make the iteration happen
        return self

    def __next__(self):     #
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val      # eventual value of topten @ each iteration
        else:
            raise StopIteration

values = topten()

# print (next(values))

for i in values:
    print(i)