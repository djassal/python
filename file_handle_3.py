def readfile(file_name):
    file = open(file_name)
    print(file.readlines())

def writefile(file_name):
    file = open(file_name,"w")
    file.write(input("Please enter your name: "))

def copyfile(num):
    file = open("real_estate.csv","r")
    new_file = open("backup_real_state.csv","w")
    count = 0
    header = file.readline()
    new_file.write(header)
    for val in file:
        new_file.write(val)
        count = count + 1
        if count == num:
            break
    file.close()
    new_file.close()
    
print("Choose your option:- ")
print("1. Read Operation")
print("2. Write Operation")
print("3. Copy n lines of files from from real_estate.csv to backup_real_estate.csv")
try:
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        file_name = input("Please enter the filename: ")
        readfile(file_name)
    elif choice == 2:
        file_name = input("Please enter the filename: ")
        writefile(file_name)
        print("File created successfully.")
    elif choice == 3:
        limit = int(input("Please enter the number of lines you wish to copy: "))
        copyfile(limit)
        print("File created successfully.")
    else:
        print("Invalid Choice, please check again.")

except FileNotFoundError :
    print("File not found please check again..........")
except TypeError :
    print("Please check your input again..........")
except ValueError :
    print("Please check your input again..........")
except :
    print("Something else went wrong...............")
    
finally:
    print("End of Program...................")