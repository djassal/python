import os
import calendar as c
import datetime as d
import time
import shutil as s
def information():
    print("Current working directory: ", os.getcwd())
    print("Current Username: ", os.getlogin())
    print("Current process id: ", os.getpid())
    today = d.datetime.now()
    ts = time.time()
    print("Today's Tme: ", today)
    print("Today's Tmestamp : ", ts)
    print(c.month(2019,7))
    print(c.calendar(2018))
    print(os.getenv('PATH'))
    
def make_archive():
    s.make_archive("test","zip","C:\\Users\\Administrator\\Desktop\\Python_Training_Deloitte")
    print("Archive Created")

information()
#make_archive()
