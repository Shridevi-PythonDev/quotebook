import pandas

df1 = pandas.DataFrame([[2, 4, 8], [10, 20, 30]], columns = ["Name", "Age", "Value"], index = ['first', 'second'])
print(df1)

'''
df2 = pandas.DataFrame([{"Name": "Sam", "SurName": "Sing"}, {"Name": "Hari", "SurName": "Patil"}])
print(df2)


data = {'Student_Name': ['Sam', 'Priya', 'Riya', 'Hari'], 'Year': [1, 5, 7, 8], 'grades': [9.9, 9.7, 9.8, 8.9]}
df3 = pandas.DataFrame(data)
print(df3)

print(type(df1))
'''
#print(dir(df1))
print(df1.mean())

print("Mean of Data Frame 1: ", df1.mean().mean())
print(type((df1.mean())))

print(df1)
print(type(df1.Age))

print(df1.Age)
print(df1.Age.max())














