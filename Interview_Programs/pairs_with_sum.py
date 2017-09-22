
def find_pair_with_dict(arr, sum):
    my_dict = {}
    for i in range(0, len(arr)):
        my_dict[arr[i]] = i
    print(my_dict)
    for i in range(0, len(arr)):
        if my_dict.get(sum-arr[i]) != None:
            print(arr[i], sum-arr[i])

def find_pair_with_dict2(arr, sum):
    # store each element in the array in a dict
    my_dict = {}
    for i in range(0, len(arr)):
        if arr[i] not in my_dict:
            my_dict[arr[i]] = 0
        else:
            my_dict.update({arr[i]: my_dict.get(arr[i]) + 1 })

    # print(my_dict)
    for i in range(0, len(arr)):
        if my_dict.get(sum-arr[i]) != None:
            if sum-arr[i] != arr[i]:
                print(arr[i], sum-arr[i])


def find_pair_in_sorted_array(arr, sum):
    start = 0
    end = len(arr)-1
    for i in range(0, len(arr)):
        if arr[start] + arr[end] == sum:
            print(arr[start], arr[end])
            start+=1
            end-=1
        elif arr[start] + arr[end] > sum:
            end-=1
        elif arr[start] + arr[end] < sum:
            start+=1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 3, 0, 5, -10, 15]
    sum = 5
    find_pair_with_dict(arr, sum)
    print('*' * 20)
    find_pair_in_sorted_array(sorted(arr), sum)
    print('*' * 20)
    find_pair_with_dict2(arr, sum)
