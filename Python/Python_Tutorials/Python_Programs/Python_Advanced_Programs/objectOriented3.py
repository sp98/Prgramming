class A:
    def testA(self):
        print('using A')


class B(A):
    # def testA(self):
    #     print('using B')
    pass


class C(A, B):
    # def testA(self):
    #     print('using C')
    pass

if __name__ == '__main__':

    C().testA()