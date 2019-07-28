alist = [10,20,30,40]
blist = []
for val in alist:
    blist.append(val + 5)
print(blist)


def increment(x):
    return x + 5
print(list(map(increment,alist)))


alist = [10,20,30,40]
increment = lambda x: x+5
print(list(map(increment,alist)))