data = "some raw data to be displayed"

# no need to close the file existly. File is closed when the block ends.
with open("/Users/santosh/Downloads/Songs/test.mp3", 'rb') as file1:
    print(str(file1.read(16)))

# with open("text1.txt" , 'w') as with_as_write:
#     with_as_write.write(data)
#
# with open("text1.txt" , 'r') as with_as_read:
#     print (str(with_as_read.read()))


# def bits(f):
#     bytes = (ord(b) for b in f.read())
#     for b in bytes:
#         for i in range(8):
#             yield (b >> i) & 1
#
# for b in bits(open('/Users/santosh/Downloads/Songs/test.mp3', 'rb')):
#     print(b)
