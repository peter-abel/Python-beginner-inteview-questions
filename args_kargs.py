
''''*args(non-keyword arguments)  & **kwargs(key word arguments)'''
import random

'''Since *args allows you to pass in any non-keyword arguments , 
   you can add a string as an argument to your funtion just like below, 
   remember return value is a tuple'''

def generate_random(*args):
    nums = range(0,100)
    random_num = random.choice(nums)
    return *args , random_num


print(generate_random("number is:"))


'''' both *args and **kwargs can be used in a function but *args must be put before **kwargs.'''

def both(*args,  **kwargs):
  
   print(args)
   print("name is abel")
   print(kwargs)
both( Age=24, rank="intermediate")