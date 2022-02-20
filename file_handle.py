
f = open('E:\PycharmProjects\pythonProject\MyData.txt','r')
"""
print(f.read())
print(f.readline())
"""
f1=open('E:\PycharmProjects\pythonProject\MyData1.txt','w')
f1.write('something is happening\n')
f1.write('in America, ')    # w- wirte, a- append

f1=open('E:\PycharmProjects\pythonProject\MyData1.txt','a')
f1.write('that\'s great')