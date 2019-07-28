import pymysql
import os
def read_database(db):
    cursor = db.cursor()
    query1 = "select * from cust_info"
    cursor.execute(query1)
    file = open("new_real-estate.csv","w")
    for record in cursor.fetchall():
        line = ",".join(list(map(str,record)))
        file.write(line + "\n")
#        print(list(map(str,record)))
    print("File created successfully in ",os.getcwd())
    file.close()

if __name__ == "__main__":
    db = pymysql.connect(host = 'localhost', user = 'root', password = 'sudo',database = 'real_estate')
    read_database(db)