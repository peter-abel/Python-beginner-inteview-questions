 
def permutations(x):
    if len(x) <=1:
        return set(x)
    a = permutations(x[1:]) 
    b = set()
    for i in a:
        for j in range(0,len(i)+1):
            k = i[:j] + x[0] + x[j:]
            b.add(k)   
    return b

print(permutations('abel'))    