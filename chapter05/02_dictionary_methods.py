myDict = {
    'name': 'Rakib',
    'age': '23',
    'city': 'New York',
    'anotherDict': {'harry': 'potter'}
}
# print(type(myDict.keys())) # <class 'dict_keys'>
# print(list(myDict.keys())) 
# print(myDict.values()) 
# print(myDict.items()) 
# myDict.update({'fullname': 'RakibHassan'})  # add new key-value pair
# print(myDict)

print(myDict.get('name')) #  Print the value of the key 'name'
#The Difference between get() and [] is that get() returns None if the key is not found, while [] will raise a KeyError exception.
# print(myDict.get('name2'))  # None
# print(myDict['rakib'])   # KeyError