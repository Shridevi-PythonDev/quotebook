### input()

input("Enter Your Name: ")
myinput = input("Enter a String: ")
print("Entered String is:", myinput)

print(type(myinput))
my_int = int(myinput)
my_float = float(myinput)
print(type(my_int), type(my_float), my_int, my_float)


#### String Formatting
#print("\n String Formatting")
name = "Python"
print("I am %s, I work for" %name)

#### Format method
print("\n format")
price = 25
txt = "The Price is {} rupees"
print(txt.format(price))

txt = "The Price is {:.2f} rupees"
print(txt.format(price))

### Multiple Values
quantity = 3
items = 567
price = 49.898

myorder = "I want {} pieces of item number {} for {:.3f} rupees"
print(myorder.format(quantity, items, price))

#### 
print("\n Dictionary Formatting \n ")
phone_nembers = {"John Smith": "+3333234", "Sam Hari": "+9123456", "Hari Hari": "+234567"}

for pair in phone_nembers.items():
    print("{} has a phone number {}".format(pair[0], pair[1])) 

print("\n key and values formatting\n")
for key, value in phone_nembers.items():
    print("{} has a phone number {}".format(key, value))

print("\n datetime")
import datetime
print(datetime.datetime.now())















