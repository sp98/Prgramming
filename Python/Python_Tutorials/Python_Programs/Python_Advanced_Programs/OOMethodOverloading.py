
'''
We can't have two methods with same name in a class.
For methodoverloading we need to use default arguments.
'''
class MethodOverloadingDemo:
    def overloadedMethod(self, a=10):
        print(a)

if __name__ == '__main__':
    m = MethodOverloadingDemo()
    m.overloadedMethod()
    m.overloadedMethod(20)
