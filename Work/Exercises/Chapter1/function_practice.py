# function practice

import math
import urllib.request

# u=urllib.request.urlopen('http://www.python.org/')
# data=u.read()
#print(data)

x=math.sqrt(10)
#print(x)

def sumcount(n):
    '''
    Returns the sum of the first n integers
    '''
    total=0
    while n>0:
        total +=n
        n-=1
    return total

a=sumcount(4)
#print(a)

try:
    int('N/A')
except ValueError:
    print("Couldn't convert string")

raise RuntimeError("What a kerfuffle")
