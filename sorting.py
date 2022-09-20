import random

#select random numbers from a list and then sort them
list = []
for i in range (1,500):
    list.append(i)

l = []    
#populate l with random numbers
while len(l) <=200:
    nambas = random.choice(list)
    l.append(nambas)
    #l.sort()

print(l)
   
       
