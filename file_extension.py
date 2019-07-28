a = input("Enter file name: ")
if a.endswith('y'):
    print("Python File")
elif a.endswith('l'):
    print("Perl File")
elif a.endswith('c'):
    print("C lang file")
elif a.endswith('n'):
    print("JSON File")
else:
    print("Wrong Choice")