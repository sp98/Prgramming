import re

test_file = open('text1.txt', encoding = "utf-8")   #test_file is now a pointer the actual file in the file system
data = test_file.read()

test_file.close() #We should close any file are we are done using it.


print(data)

print(re.match(r'some', data))  #match only matches the first word of the text
print(re.match(r'raw', data))   #returns none with the file match is not done

print (re.search(r'data', data))  #search method searches in the first line.
print(re.findall(r'data', data))  #this method searches for in the entire module.

print(re.findall(r'[is]', data))
print(re.findall(r'[0-9]', data))
print(re.findall(r'[1-2]', data))

print(re.findall(r'\B', data))
print(re.findall(r'\w{1,3}', data))
print(re.findall(r'\w{6,}', data))
print(re.findall(r'\b', data))
print(re.findall(r'\B', data))
print(re.findall(r'\w?', data))
print(re.findall(r'\w*', data))

print(re.findall(r'[^a-z]', data))