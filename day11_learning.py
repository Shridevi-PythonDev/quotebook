'''
### List Comprehensions

my_list = [222, 333, 4444, 354, 666, 778]

temp_list = []
for temp in my_list:
    temp_list.append(temp/10)
print(temp_list)

####
my_list1 = [temp/10 for temp in my_list]
print(my_list1)

######
my_string = []
for x in "Python":
    my_string.append(x)
print(my_string)

### List Comprehension
new_letters = [letter for letter in "Python"]
print(new_letters)

### if

num_list = [num for num in range(20) if num % 2 == 0]
print(num_list)


### 
new_list = [122, 333, 444, 555, 666, -777, 888, 999]
new_temps = [temp/10 for temp in new_list if temp != -777]
print(new_temps)

###### Nested If
num_list = [x for x in range(100) if x % 2 == 0 if x % 5 == 0]
print(num_list)

### if ... else ....
new_list = [122, -333, 444, -555, 666, -777, 888, 999]
new_temps = [temp/10 if temp > 0  else 0 for temp in new_list]
print(new_temps)

mylist = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(mylist)

### Dictionary
squares = {x:x*x for x in range(10)}
print(squares)

'''
### Errors
#Syntax Errors
print(4)
int(8)
int(8)
print(6)
list = [1, 2, 3]

### Run Time Errors
a = 10
b = "10"
c = 20
print(str(a)+b)
## arguments more, unsupported type : Type error, NameError , ZeroDivisionError:

def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "The Zero dvision is meaningless"

print(divide(1,4))
print("hello")
###Try and ex except


x = 10
y  = 7
try:
    z = x/y
except ZeroDivisionError:
    z = 0
print(z)









































































































