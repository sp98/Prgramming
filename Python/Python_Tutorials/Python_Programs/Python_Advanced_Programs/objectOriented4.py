'''
Usage of private acccess modifier in python
'''

class Parent:
    def my_method(self):
        print('I am in parent')

    def __my_private_method(self):
        print('I am a private method in the parent')

if __name__ == '__main__':
    obj= Parent()
    obj.my_method()
    # obj.__my_private_method()   This gives error.
    obj._Parent__my_private_method()   # private method can be accesed via - object._ClassName__method_name()

