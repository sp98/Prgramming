

def iterative_reversal(arr):
    size = len(arr)
    start = 0
    end = size-1
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

def recursive_reversal(arr, start, end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    recursive_reversal(arr, start+1, end-1)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 2, 10, 14]
    print(iterative_reversal(arr)) # iterative reversal.
    print(arr[::-1]) # pythonic way
    recursive_reversal(arr, 0, len(arr)-1) # recurive Reversal
    print(arr)
