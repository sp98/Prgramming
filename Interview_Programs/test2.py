def findit(a, k):
    length = len(a)
    count = 0
    for x in range(length):
        for y in range(x, length):
            if a[x] + k == a[y] or a[x] - a[y] == k:
                count = count + 1
    return count
print(findit([5, 1, 5, 3, 4, 2], 2))
