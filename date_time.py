import datetime
today = datetime.date.today()
name = today.strftime("%d_%b_%Y")
file = open(name + ".txt","w")
file.close()