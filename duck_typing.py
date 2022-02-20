
class PyCharm:
    def execute(self):
        print('compiling')
        print('running')

class MyEditor:
    def execute(self):
        print('spell check')
        print('conv. check')
        print('compiling')
        print('running')

class laptop:
    def code(self,ide):
        ide.execute()

ide = MyEditor()

lap1 = laptop()
lap1.code(ide)
