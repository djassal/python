import pymysql
import os
import csv
def create_database(db):
    cursor = db.cursor()
#    query = "create database real_estate"
    query1 = "create table cust_info(Street varchar(200), City varchar(100), Zip int, State varchar(200), Beds int, Baths int, Type varchar(200), Price int)"
    cursor.execute(query1)
 
def insert_data(db):
    try:
        cursor = db.cursor()
#        index = 0
        file_name = input("Please enter file name: ")
        if os.path.isfile(file_name):
            file = open(file_name,"r")
            reader = csv.reader(file)
            file.readline()
            for val in reader:
                query = "insert into cust_info value('{}','{}',{},'{}',{},{},'{}',{})".format(val[0],val[1],val[2],val[3],val[4],val[5],val[7],val[9])
#                cursor.execute(query.format(val.split(",")[index],val.split(",")[index+1],val.split(",")[index+2],val.split(",")[index+3],val.split(",")[index+4],val.split(",")[index+5],val.split(",")[index+7],val.split(",")[index+9]))
                cursor.execute(query)
            db.commit()     
            file.close()
            print("Entries added successfully.")
        else :
            print("File does not exist.")
    
    except FileNotFoundError:
        print("File not found please check again............")
    except TypeError :
        print("Please check your input again..........")
    except NameError :
        print("Something is not defined in program..........")
    except:
        print("Something went wrong............")
    

if __name__ == "__main__":
#    db = pymysql.connect(host = 'localhost', user = 'root', password = 'sudo')
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'sudo',database = "real_estate")
    insert_data(db)
#    create_database(db)