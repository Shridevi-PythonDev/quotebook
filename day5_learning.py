tempratures = [9.4, 10.5, 20.3, 8.4, 7.8, 1, 3, 5, 6, 7.7, 8.8 ]
### Slicing
print(tempratures[1:4])
print(tempratures[3:])
print(tempratures[:8])

### Negative Slicing
print(tempratures[-1])
print(tempratures[-5])
print(tempratures[0:-1])
print(tempratures[-4:-2])
print(tempratures[-5:])
print(tempratures[:-1])

### String Slicing
tempratures1 = ["Python", 9.4, 10.5, 20.3, 8.4, 7.8, 1, 3, 5, 6, 7.7, 8.8 ]
print(tempratures1[0])
print(tempratures1[0][3])
print(tempratures1[0][-1])
print(tempratures1[0][1:4])
print(tempratures1[0][-3:])

### List to Tuple
my_list = [1, 2, 3]
print(tuple(my_list))
my_tuple= tuple(my_list)
print(my_list)
print(my_tuple)

### Tuple to List
data = (10, 12, 14, 15)
print(data)
print(type(data))
data_list = list(data)
print(data_list)
print(type(data_list))

#### List to Dictionary
data = [['name', "John"],['surname', 'Smith']]
my_dict = dict(data)
print(my_dict)

#### Funcions
print("\n\n****Functions******\n")


def hello():
    print("hello")
    sum1 = 2+3
    return sum1

print(hello())


#### Mean/Average
student_grades = [9.5, 8.9, 7.5]
my_sum = sum(student_grades)
length = len(student_grades)
my_mean = my_sum/length
print(my_mean)


print("\n*** Mean**")
def my_mean(my_list):  
    the_mean = sum(my_list)/len(my_list)
    return the_mean

student_grades = [9.5, 8.9, 7.5]
print("Mean of Student Grades: ", my_mean(student_grades))

print(type(my_mean), type(sum) )










































