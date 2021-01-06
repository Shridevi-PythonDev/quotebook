### Conditions
# if

a = 90
b = 60

if b<a:
    print("Yes a is greater than b")
    print(b)
    print(a*b)

else:
    print("b is greater")
    print(a)

#### elif
a = 25
b = 18

if b > a:
    print("if condtion, b greater")

elif a == b:
    print("you are in elif condition, equal")

else:
    print("else condition, a is greater")

### and
a = 200
b = 30
c = 20

if a>b and c>b:
    print("b is smallest, AND condition")

else:
    print("b is not smaller")

### OR

a = 200
b = 30
c = 20

if a>b or c>b:
    print("b is smallest, OR condition")

else:
    print("b is not smaller")


### While loop

x = 1

while x < 3:
    print("you are in while", x)
    x = x + 1
    print(x)

##### Infinite

#while True:
#    print("you are in while")

## While and Else

count = 0
while count < 5:
    print(count, "is lesser than 5")
    count = count + 1

else:
    print(count, " You are in else ")

### For loop
fruits = ["apple", "banana", "cherry"]

for temp in fruits:
    print(temp)
    
    for x in temp:
        print(x)

#####  Control Statements::
### Break in For loop

for letter in "Python":
    if letter == 'h':
        break
    print("current letter", letter)

## Break in While

var = 10
var = 5
while var > 0:
    print("Current variable value: ", var)
    ##var = var - 1
    if var == 5:
        break

    print("after break")

### Continue
#
for letter in "Python":
    if letter == 'h':
        continue
    print("current letter", letter)
    




var = 10

while var > 0:
    print("Current variable value: ", var)
    var = var - 1
    if var == 5:
        continue

























       














