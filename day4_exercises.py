
#### Dictionary 
###Assign a dictionary to variable . The dictionary should contain 3 keys with 
# names and each key should have a float value

day_temperatures = {
                    'morning' : 10.4,
                    'noon' :  30.4, 
                    'evening': 28.8
                   }
print(day_temperatures)


#### Create a dictionary with name, age and class and print them 
dict1 = {'Name': 'Siya', 'Age': 7, 'Class': 'First'}
print( "dict1['Name']: ", dict1['Name'])
print( "dict1['Age']: ", dict1['Age'])


#### Tuple colour_codes
colour_codes = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(colour_codes)

### dictionary inputs Tuple
day_temperatures = {'morning': (1.2, 2.1, 3.3), 'noon': (2.3, 3.3, 4.5), 'evening': (2.4, 5.6, 7.8)}
print(day_temperatures)

#### append
seconds = [1.233, 1.333, 1.555, 1.098]
current = 2.333
seconds.append(current)
print(seconds)

###remove

seconds.remove(1.555)
print(seconds)

#### index
tempratures = [9.4, 10.5, 20.3, 8.4]
print(tempratures[0])
print(tempratures.index(20.3))
print(tempratures[2])
print(tempratures[3])

#####
workdays = ["Mon", "Tue", "wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])
workdays.append(weekend[1])
print(workdays)







