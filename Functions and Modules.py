'''
Fucntions and Modules
v1.0
Beck Utigard
'''

from random import * # * is a wild card meaning everything
# Imports should always be at the top of your program
from math import pi
#from math import *
import my_module

# When you use keyword from, you are importing directly into your file
# (no need to use random.randrange, just use randrange)

# Functions and Modules
print(randrange(900, 1000))

if __name__ == "__main__":
    '''
    This code only runs if this is the executed code/file.
    '''
    print(randrange(100))
    print(random())
    print(pi)

    e = 5
    print(e)

    print("\n")

    print("This is period", my_module.period)
    my_module.hello("Beck")
    product, sum = my_module.product_sum(10, 20)
    print(product, sum)