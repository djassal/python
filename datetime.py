import datetime as d
import time
today = d.date.today()
def datetime_practice():
    print(today)
    print(today.strftime("%B %d %Y"))
    print(today.strftime("%d %b %Y"))
    print(today.strftime("%m %d %y"))
    print(today.strftime("%b %d %Y"))
    print(today.strftime("%B %D %Y"))
    print(time.time())
    print(d.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

def delta_use():
    tod = d.date.today()
    yes = tod - d.timedelta(days = 1)
    tom = tod + d.timedelta(days = 1)
    print(tod)
    print(yes)
    print(tom)
    print("Time between tomorrow and yesterday: ",tom - yes)
    
day_delta = d.timedelta(days = 1)
#print(day_delta)
start_date = d.date.today()
end_date = start_date + 7*day_delta
for i in range((end_date - start_date).days):
    print(start_date + i*day_delta)
    
#print(d.datetime.now().strftime("%A"))   
#datetime_practice()
#delta_use()
