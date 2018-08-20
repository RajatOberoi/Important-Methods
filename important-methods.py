#Ques1
a=[]
x=int(input("enter no of element in list"))
for i in range(x):
    c=int(input("enter the no"))
    a.append(c)
print(a)
#after reversing the list
a.reverse()
print(a)
a.reverse()
print(a)
#another method for reversing is
print(a[::-1])


#Ques2
y=input("enter any string")
print("string is",y)
for i in y:
    if i>="A" and i<="Z":
        print("upper case letters are",i)

    
    
#Ques3
z=input("enter no using commas")
d=z.split(',')
print(d)
b=[]
for i in d:
    s=int(i)
    b.append(s)
print(b)    


#Ques4
v=input("enter string")
if v==v[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

#Ques5
#In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.
# Python code to demonstrate copy operations
 
# importing "copy" for copy operations
import copy
 
# initializing list 1
list_1 = [1, 2, [5,6,7], 4]
 
# using deepcopy to deep copy 
list_2 = copy.deepcopy(list_1)
 
# original elements of list
print ("The original elements before deep copying")
for i in range(0,len(list_1)):
    print (list_1[i],end=" ")
 
# adding and element to new list
list_2[2][1] = 8
 
# Change is reflected in list_2 
print ("The new list of elements after deep copying ")
for i in range(0,len( list_1)):
    print (list_2[i],end=" ")
 
 
# Change is NOT reflected in original list
# as it is a deep copy
print ("The original elements after deep copying")
for i in range(0,len( list_1)):
    print (list_1[i],end=" ")

#The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
#A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
#A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.
