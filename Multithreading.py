from threading import *
from time import sleep
class Eating(Thread):
    def run(self):
        for i in range(6):
            print("Eating!!!")
            sleep(1)
          
class Watching(Thread):
    def run(self):
        num2=5
        for i in range(6):
          print("Watching Mobile!!!")
          sleep(1)
obj1=Eating()
obj2=Watching()
obj1.start()
sleep(0.2)
obj2.start()
obj1.join()
obj2.join()
print("Bye!!!")
