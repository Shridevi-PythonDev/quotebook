### File Handling

### Opening file
## Reading a file
### File Cursor

myfile = open("file.txt", "r")
#print(myfile.read())

content = myfile.read()
print(content)
#print(content)

### Close File
myfile.close()

### With 
with open("file.txt") as my_file:
    content = my_file.read()
print(content)
'''
#### Writing in File 
#myfile = open("file.txt", "w")
### Different file paths

with open("E:\Python_Coding\myfile.txt","w") as my_file:
    my_file.write("Python World\n")
    my_file.write("Write write and keep writing")

'''
with open("E:\Python_Coding\myfile.txt","a+") as my_file:
    my_file.write("\nBye\n")
    my_file.write("Hi")
    my_file.seek(0)
    content = my_file.read()
    #print(content)

### Seek() to set the postion
print("Name of the file: ", my_file.name)
### closed
print("Closed or Not: ", my_file.closed)

### Check Mode
print("Opening Mode: ", my_file.mode)


with open("E:\Python_Coding\myfile1.txt","x") as my_file:
    my_file.write("\nBye\n")
    my_file.write("Hi")










































