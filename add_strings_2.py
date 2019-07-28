domains = ["google","www.unix","oracle.com"]
for x in range(0, len(domains)):
    if not "com" in domains[x] and not "www" in domains[x]:
       print("www." + domains[x] + ".com")
    elif not "www" in domains[x]:   
        print("www." + domains[x])
    elif not "com" in domains[x]:
       print(domains[x] + ".com")
 