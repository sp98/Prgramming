
'''
About method overloading and overriding.

'''
class Parent:
    def method1(self, i=10):
        print('Overloaded method1 for the value ' + str(i))

    def method2(self, *args):
        for arg in args:
            print('Overloaded method2 for the value ' + str(arg))


class Child(Parent):
    def method1(self, i=10):
        print('Overridden method1 for the value ' + str(i))

    def method3(self, *args):
        print('Only child class has this method')

if __name__ == '__main__':
    p = Parent()
    p.method1()
    p.method2(3,4,5)
    p.method2('santosh', 'pillai')

    print("*** Overriding ***")
    p.method1(10)

    c = Child()
    c.method1()
    c.method2(3)
    c.method3(4)