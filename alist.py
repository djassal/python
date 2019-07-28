alist = ["unix","unix","oracle","oracle","oracle","java","python","hadoop"]
dic = {}
for index in range(0, len(alist)):
    dic[alist[index]] = alist.count(alist[index])
for x in dic:
    print(x,"-",dic.get(x))
print("-------------------------------------")

for item in set(alist):
    print(item,":",alist.count(item))
print("-------------------------------------")

import collections
infolist = collections.Counter(alist)
for value in infolist:
    print(value,"-",infolist[value])
