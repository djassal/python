file = open("demo_file_handling.txt",'w')
file.write("This is a test file.\n")
file.write("1. Python.\n")
file.write("2. Rust.\n")
file.write("3. Golang.\n")
file.write("4. R \n")
file.close()

file = open("demo_file_handling.txt",'r')
print(file.read())
file.close()
