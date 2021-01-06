#### String Operations

def string_oper(mystring):
    
    if len(mystring) == 8 or len(mystring) > 8:
        return "TRUE"
    
    else:
        return "FALSE"

print(string_oper("hey"))

#### For and While loops
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)

#colors = [11, 34, 98, 43, 45.9, 54, 54, "pi"]
for color in colors:
    if isinstance(color, int):
        print(color)

print("\n AND ")
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

### Nested Loops to print the pattern

print("\n Pattern FOR")

for i in range(1,6):
    for j in range(i):
        print("*", end=' ')
    #print()
    print("\r")


print("\n Pattern WHILE")
i = 6
while(i > 0):
    j=6
    while(j>i):
        print("*", end=' ')
        j = j-1
        
    i-= 1
    print()






