### Dictionary

my_dict = {'Name': 'Riya', 'Age': 8, 'Class': 'First'}

print(my_dict.items())

print(my_dict.keys())

print(my_dict.values())

### Update existing Entry
my_dict['Age'] = 9
print(my_dict)

## Add New Entry
my_dict['School'] = 'Gov School'
print(my_dict)

## Remove 'Name'
del my_dict['Name']
print(my_dict)

##print(my_dict['Age'])

### Clear All Entries
my_dict.clear()
print(my_dict)

## Del Complete Dictionary
del my_dict
## print(my_dict)


##Tuple
tup = (1, 2, 3, 4, 5, 6, 7)
print("tup[3]", tup[3])

print(tup[2:6])

tup1 = (12, 40.3, 8, 9, 18, 14, 16)
tup2 = ('abc', 'xyz')


###  tup1[0] = 180
## Adding Tuples
tup3 = tup1 + tup2
print(tup3)

















