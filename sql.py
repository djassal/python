import pymysql

def connectdb(db):
    print(db)
    cursor = db.cursor()
#    query = "create database deloitte"
    query1 = "create table empinfo(first_name varchar(100), last_name varchar(100))"
    cursor.execute(query1)

def insert_records(db):
    try: 
        for count in range(0,int(input("Enter number of records: "))):
            cursor = db.cursor()
            f_name = input("Please enter firstname: ")
            l_name = input("Please enter lastname : ")
            query = "insert into empinfo value('{}', '{}')"
            cursor.execute(query.format(f_name,l_name))
        db.commit()

    except ValueError:
        print("Please enter an integer value for number of records.")
    except :
        print("Something went wrong.........")
    
if __name__ == "__main__":
#    db = pymysql.connect(host = 'localhost', user = 'root', password = 'sudo')   // for creating database
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'sudo',database = "deloitte")
#    connectdb(db)
    insert_records(db)