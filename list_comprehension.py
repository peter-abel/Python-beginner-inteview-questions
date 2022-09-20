#creating an empty list
list = []
for i in range (0,20):
    list.append(i)

#even numbers in the list
even = [num for num in list if num%2==0 ]
#odd = [num for num in list if num%2!=0]
print(even)
#print(odd)

#squares of the even list
squares = [ num**2 for num in even]

print(squares)

