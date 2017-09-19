
def gcd(n, d):
    for i in range(1, n+1):
        if n % i == 0 and d % i == 0:
            return i

def gcd2(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b > 0:
        return b
    if b == 0 and a > 0:
        return a

    if a == b:
        return a
    if a > b:
        return gcd2(a-b, b)
    return gcd2(a, b-a)

def rotation (arr, n, k, s):
    for i in range(0, s):
        temp = arr[i]
        print('temp : ' + str(temp))
        for j in range(i, n):
            d = (j+k) % n
            print(d)
            arr[j] = arr[d]
            print(arr)
            #j = d
            if d == i:
                print(j)
                arr[j] = temp
    return arr



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    k = 2 # the rotation number
    s = gcd2(n, k)
    print('GCD is :' + str(s))
    print(rotation(arr, n, k, s))
