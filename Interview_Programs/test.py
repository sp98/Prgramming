def findit(x):
   myStr = str(x)[::-1]
   length = len(my_str)
   mylist = [ myStr[x:y] for x in range(length) for y in range(x, length) if myStr[x:y] >]


print(findit(12121212121213434343))
