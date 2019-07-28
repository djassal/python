file = open("even_number_reverse.txt","w")
for x in range(1001,499,-1):
    if x % 2 == 0:
        file.write(str(x) + "\n")
file.close()
