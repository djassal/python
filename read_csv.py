try: 
#    file_name : real_estate.csv
#    file_name = input("Please enter your filename: ")
    file = open("real_estate.csv","r")
    list_city = []
    count = 0
    for val in file:
        b = val.split(',')[1]
        if b == "city":
            continue
        list_city.append(b)
        count = count + 1
    print(list(set(list_city)))
#    li_city = list(set(list_city))
#    for x in range(0,len(li_city)):
#        print(li_city[x])
    print("Total no. of records in real_estate.csv are: ",count)
    file.close()
    
except FileNotFoundError : 
    print("File not found please check again..........")

finally:
    print("End of program.........")