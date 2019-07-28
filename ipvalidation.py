ip = input("Enter any IP address: ")
for x in range(0, len(ip.split("."))):
    i = int(ip.split(".")[x])
    if i < 999 and i > 0:
        if x < int(len(ip.split("."))-1):
            continue
        print("It's valid IP. ")
    else:
        print("Invalid IP")
        break
