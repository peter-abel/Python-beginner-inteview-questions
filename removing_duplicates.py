#the set method allows one to remove duplicates from a list
l = list(range(10)) + list(range(10))
print(l)
ls = list(set(l))
print(ls)