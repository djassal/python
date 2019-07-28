import threading

class Thread1(threading.Thread):
    def run(self):
        i = 1
        while i <=100:
            print("Value of i :",i," ")
            i = i + 1


class Thread2(threading.Thread):
    def run(self):
        j = 101
        while j <= 200:
            print("Value of j :",j ," ")
            j = j + 1


t1 = Thread1()
t2 = Thread2()

t1.start()
t2.start()              
