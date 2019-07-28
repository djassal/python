ip2 = "192.168."
for x in range(1,21):
    first_ip = ip2 + str(0) + "." + str(x)
    if x > 10:
        first_ip = ip2 + str(1) + "." + str(x-10)
    print(first_ip)
