def merge(a,b):
    """ Function to merge two arrays """
    print('Inside Merging')
    print(a)
    print(b)
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    print(c)
    return c

# Code for merge sort

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    print('Current Value  of x -- ')
    print(x)
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        print('*' * 10)
        print(middle)
        a = mergesort(x[:middle])
        print('time to check value b')
        b = mergesort(x[middle:])
        print(a)
        print(b)
        print('*' * 10)
        return merge(a,b)


my_list = [2, 3, 100, 1, 4, 9, 10]
print(mergesort(my_list))
