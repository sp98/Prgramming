'''
Modes:
'r': for reading. This is default. File should pre exist.
'w': for writing. It trucates (deletes content) for the file first.
'a': for appending. It adds to the existing data of the file.
'''

name = 'Santosh Pillai'
my_file = open("text1.txt" , "a")

my_file.write(name + '\n')

my_file.close()

my_file1 = open("text1.txt" , 'r')
print(str(my_file1.read()))
my_file1.close()


# my_file2 = open ("/Users/santosh/PycharmProjects/Advanced1/Test" , 'r')
# print(my_file2.read())
# my_file2.close()
#
#
# my_file2 = open ("/Users/santosh/PycharmProjects/Advanced1/Test" , 'r')
# print(my_file2.readline())
# my_file2.close()
