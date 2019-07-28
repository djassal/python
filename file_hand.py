try: 
    file = open("real_estate.csv","r")
    new_file = open("backup_real_state.csv","w")
    header = file.readline()
    new_file.write(header)
    for val in file:
        if val.split(",")[1] == "SACRAMENTO":
            replaced_list = val.replace("SACRAMENTO","MUMBAI")
            new_file.write(replaced_list)
    file.close()
    new_file.close()

except FileNotFoundError:
    print("File not found please check again.........")
except Exception:
    print("Something else  went wrong.........")

finally:
    print("End of Program..........")
