'''### create new file and read
file = open("myfile.txt")
content = file.read()

#### printout 50chars
print(content[:100])

#### create a file and write
with open("new_file.txt", "x") as mynewfile:
    mynewfile.write("Python World")
'''
### read from file1 and write to file2
with open("file1.txt") as myfile:
    content = myfile.read()

with open("file2.txt", "a+") as file:
    file.write("\n")
    file.write(content)





