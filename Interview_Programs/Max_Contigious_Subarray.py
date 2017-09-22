
def kadane_alog(arr, size):
    max_so_far = 0
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
            s = i+1
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return max_so_far, arr[start:end+1]


if __name__ == '__main__':
    arr = [11, -12, -1, -4, 5, 11, 18]
    print(kadane_alog(arr, len(arr)))
