# Use open function to read the content of a file!
f = open('sample.txt', 'r')
# data = f.read() # read the entire file
data = f.read(5) # read first 5 characters
print(data) # print the data
f.close() # close the file