d = {"c1":10, "c2":20, "c3":30}
n = {1:2, 3:4, 5:6}
n2 = {10:[2,3,4], 20:[4,5,6], 30:[6,7,8]}
print(d["c1"])
print(n2[20])
#print(n2.pop(10))
print(d.keys())
print(d.values())
print(d.items())
print(n2.keys())
print(n2.values())
print(n2.items())
d["c4"] = (10,20,30)
print(d.values())
