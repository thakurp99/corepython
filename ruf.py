'''

import threading
import time
from threading import *

def Emp():
    for i in range(1,5):
        print("Hello i am python",i)
        time.sleep(1)

def Worker():
    for i in range(1,11):
        print("Working......",i)
        time.sleep(2)

a1 = threading.Thread(target=Emp)
a2 = threading.Thread(target=Worker,daemon=True)
a1.start()
a2.start()
'''

a = (1,2,3,5,6)
print(type(a))


a = [1,2,3,5,6]
print(type(a))


a = {1,2,3,5,6}
print(type(a))



a = {"name":"Ram","age":23}
print(type(a))
print(a.keys())
print(a.values())




print("hello")