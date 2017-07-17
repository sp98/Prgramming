"""
A Sorting Algorithm
We navigate through each element in a loop and check if that element is larger than the next one and swap places.
In each iteration, the largest element will move towards the right. So we can decrement the iteration count by one on each iteration.

This algo is not very effecient. Its run time is o(n2)

"""

def bubble_sort(arr):
    is_sorted = False
    iteration_length = len(arr)-1
    while not is_sorted:
        is_sorted = True
        for index in range(iteration_length):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index+1], arr[index]
                is_sorted = False
        iteration_length = iteration_length - 1

    return arr

my_list = [3, 4, 5, 2, 1, 0, 100, 12121, 23, 4.5]

print(bubble_sort(my_list))
