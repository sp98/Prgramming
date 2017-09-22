"""
In a list, find all the triplets whose sum are equal to a given number
"""
def find_triplets_with_sum(arr, number):
    size = len(arr)
    for i in range(0, size-2):
        l = i + 1
        r = size-1
        while l < r:
            if arr[i] + arr[l] + arr[r] == number:
                print( str(arr[i]) + ',' +  str(arr[l]) + ',' + str(arr[r]))
                l+=1
                r-=1
            if arr[i] + arr[l] + arr[r] > number:
                r-=1
            else:
                l+=1

if __name__ == "__main__":
    arr = [ 1, 2, 3, 4, -5, 0, 0]
    number = 4
    find_triplets_with_sum(sorted(arr), number)
