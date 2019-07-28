import os
import shutil

def display_all_files():
    for file in os.listdir():
        print(file)
        
def display_cdrive_files():
    for file in os.listdir("C:\\"):
        print(file)

def display_csv_only():
    for file in os.listdir():
        if ".csv" in file: 
            print("Existing csv files: ")
            print(file)

def delete_py_files():
    os.chdir("C:\\Users\\Administrator\\Desktop\\test_py")
#    print(os.getcwd())
    for file in os.listdir():
        if ".py" in file:
            os.remove(file)
    print("All python files deleted.")
    
def file_display_size():
    for file in os.listdir("D:\\Python_Training_Deloitte"):
        if ".py" in file:
            print("Filename: ",file, ", Size: ", os.path.getsize(file), "bytes.")

def copy_files():
    for file in os.listdir("C:\\Users\\Administrator\\Desktop\\Python files\\Source"):
        shutil.copy("C:\\Users\\Administrator\\Desktop\\Python files\\Source\\" +file, "C:\\Users\\Administrator\\Desktop\\Python files\\Destination")
        print(file,"is copied to destination folder.")
        
def folder_making():
    for val in range(1,101):
        os.makedirs("dir" + str(val))

#display_all_files()
#display_cdrive_files()
#display_csv_only()
#delete_py_files()
#file_display_size()
#copy_files()
#folder_making()
