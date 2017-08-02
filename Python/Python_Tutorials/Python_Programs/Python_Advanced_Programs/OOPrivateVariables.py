class PrivateVariables:
    public_check = 1
    _private_check1 = 2
    __private_check2 = 3

if __name__ == '__main__':
    p = PrivateVariables()
    print(p.public_check)
    print(dir(p))
    print(p._PrivateVariables__private_check2)
    print(p._private_check1)
