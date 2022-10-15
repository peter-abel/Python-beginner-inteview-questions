
''''*args  & **kargs'''
import random

def generate_random(*args):
    nums = range(0,100)
    random_num = random.choice(nums)
    return *args , random_num


print(generate_random("number is:"))