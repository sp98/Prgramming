def remove_dup_after_sorting(arr):
    size = len(arr)
    j = 0    # To store index of next unique element

    for i in range(0, size-1):
        # If current element is not equal
        # to next element then store that
        # current element
        if(arr[i] != arr[i+1]):
            arr[j] = arr[i]
            j+=1

    arr[j] = arr[size-1] # Store the last element as whether it is unique or repeated, it hasn't stored previously

    return arr[0:j+1]

if __name__ == '__main__':
    arr = [10, 10, 1, 1, 1, 3, 3, 4, 5, 6, 7, 8, 8, 9]
    print(remove_dup_after_sorting(sorted(arr)))
    print(dict.fromkeys(arr, 10))


# add more ways to do this below
