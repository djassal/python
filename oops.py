import pymysql
import sys
class Database:
    def __init__(self,database_name,username,password,hostname):
        self.database_name = database_name
        self.username = username
        self.password = password
        self.hostname = hostname
        
    def connectDatabase(self):
        try:
            db = pymysql.connect(host = self.hostname, user = self.username, password = self.password ,database = self.database_name)
            print(self.database_name,"selected successfully by",self.username)
            return db
        except pymysql.err.OperationalError:
            print("Unable to connect to database due to incorrect credentials.")
            sys.exit(0)
        except pymysql.err.InternalError:
            print("Database not found.")
            sys.exit(0)
            
    def displayRecords(self,db):
          cursor = db.cursor()
          query = 'select * from cust_info'
          cursor.execute(query)
          for record in cursor.fetchall():
              print(record)
    
    def insertRecords(self,db):
        cursor = db.cursor()
        query = "insert into cust_info value('{}','{}',{},'{}',{},{},'{}',{})".format(input("S: "),input("S: "),input("Int: "),input("S: "),input("Int: "),input("Int: "),input("S: "),input("Int: "))
        cursor.execute(query)
        db.commit() 
        print("Entries added successfully.")
        
              
db_name = input("Please enter the database name: ")
host = input("Please enter the hostname: ")  
user = input("Please enter the username: ")  
pas = input("Please enter your password: ")   
data1 = Database(db_name,user,pas,host)
db = data1.connectDatabase()
print("Enter 1 to display all records.")
print("Enter 2 to insert new records.")
try:    
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        data1.displayRecords(db)
    elif choice ==2:
        data1.insertRecords(db)
    else:
        print("Incorrect choice.")
        
except ValueError:
    print("Please check your input again.")
except:
    print("Something went wrong.")