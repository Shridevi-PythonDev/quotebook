
## 1. Exercise 1
name = "Ram"
height = 5.6
age = 30

print(name, height, age)
print(type(name), type(height))
print(type(age))

##2
x = 10
y = 20.1
z = 30

sum1 = x+y+z
print("sum of 3 variables: ", sum1)


### 3 Range
print(list(range(1, 11)))

###4 
print(list(range(0, 30, 5)))

### 5
print(list(range(0, 11, 3)))

###list(range('days', 'month'))

## 6
cricket = [10.2, 90, "IPL"]
print(cricket)

## 7
temprature = [10.2, 20, "rainfal", [11, 30.2, 'rain']]
print(temprature)

## 8
mylist = [1, 2, 3, 4, 5, 6, 7]

sqr_list = [x * x for x in mylist]

print(type(sqr_list))

## 9
mylist = ["John", "", "Sam", "", "", "Ram"]
mylist_filter = list(filter(None, mylist))
print(mylist_filter)

