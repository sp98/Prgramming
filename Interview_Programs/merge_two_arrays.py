"""
Merge Two arrays into a single sorted array discarding the duplicates
"""
def merge(arr1, arr2):
    for x in arr1:
        if x not in arr2:
            arr2.append(x)
    return arr2

def sort_arr(arr):

if __name__ == '__main__':
    arr1 = [4, 5, 6, 7]
    arr2 = [5, 7, 10, 11]

    
