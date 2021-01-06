import math

num = input("Enter Num: ")
num = int(num)
print(math.sqrt(num))

### platform
import platform

print(platform.system())

### dir(__builtins__)

funs_dir = dir(platform)
print(funs_dir)






import calculation

print(calculation.sub(5, 2))
print(calculation.add(6, 4))

from calculation import sub

print(sub(6,3)) 

from calculation import *
print(mul(3, 4))



import calculation as cal
print(cal.add(x,y))


### area

def area(a , b):
    return a*b

print(area(7,9))  
#print(area(5))

def mean(*args):
    return sum(args)/len(args)

print("Mean: ", mean(7, 9, 8 , 9))

def area(a , b):
    return a*b

print(area(7,9)) 


#print(area(5))


def mean(**kwargs):
    return kwargs

print(mean(a=1, b=2, c=3, d=4)) 





































