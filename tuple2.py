tup = ("unix","hadoop","oracle","scala")
alist = list(tup)
alist.append("spark")
alist.append("ruby")
print("After appending list: ", alist)
add = ['java', 'linux', 'unix', 'C', 'C++', 'mysql', 'oracle']
alist.extend(add)
print("After addition list: ", alist)
alist.insert(4, "mongodb")
print("After insertion at index 4: ", alist)
alist.remove(alist[0])
print("After removing at index 0: ", alist)
alist1 = set(alist)
print("Final Output after removing the duplicates: ", alist1)
print("Final tuple list: ", tuple(alist1))