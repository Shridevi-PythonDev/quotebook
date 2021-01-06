str = "John"  
str2 = "ab"  
# Calling function    
str2 = str.join(str2)    
# Displaying result    
print(str2)  

even = [2,4,6,8,10,11,12,14]  
odd = 0  
for val in even:  
    if val%2!=0:  
        odd = val  
        break  
    print(val)  
print("odd value found",odd)  

a={}
a['a']=1
a['b']=[2,3,4]
print(a)

d = [ (a,b) for a in range(3) for b in range(a) ]
print(d)