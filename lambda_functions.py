
# lambda functions are anonymous function, or without names
# example 1
l = lambda a: a*2


#expected value 8
print(l(4))


#example 2
#Creates an empty list ls
ls = []
for i in range(1,21):
    # cretes a lambda funtion that adds an interger(num) to all numbers from 1 to 20
    #Useful when updating a list
    a = lambda num: num + i
    ls.append(a(2))
    print(ls)
