#Creating an empty set
b=set()
print(type(b))
#Adding values to an empty set
b.add(1)
b.add(2)
b.add((4,5,6))
# b.add({4:5}) #This is not allowed. Cannot add list or dictionary to a set
print(b)

#length of a set
print(len(b))


#Removing values from a set
b.remove(1) #Removes the first occurrence of 1
print(b)

# pop method 
print(b.pop()) #Removes and returns the last element of the set

#clear method
b.clear()   #Removes all the elements from the set
print(b)