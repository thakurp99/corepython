import threading
import time
from threading import *
'''
class Emp:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getEmp(self):
        return self.name, self.age
a = Emp("Ram",101)
print(a.getEmp())
'''
def hello(name):
    for i in range(5):

        print("Hello",i)


def hii(name):
    for i in range(5):
        print("Hyy Python",i)


a1 = threading.Thread(target=hello,args=("Ram",))
a2 = threading.Thread(target=hii,args=("Shaym",))

a1.start()
a2.start()
