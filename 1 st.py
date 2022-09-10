import threading
from threading import *
import time

def emp():
    for i in range(1,10):
        print(i,"hello")
        time.sleep(1)

def abc():
    for i in range(1,6):
        print("Hiiii.......",i)
        time.sleep(1)

t1 = threading.Thread(target=emp, daemon=True)
t2= threading.Thread(target=abc)

t1.start()
t2.start()