def strange(j):
    k = 0
    while j > 0:
        k = 10 * k + j % 10
        #print(k)
        j = j/10
        #print(j)
    return k

print(strange(1230))
