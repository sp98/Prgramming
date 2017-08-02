
class ParentOfParentOfA:
    def parentMethod(self):
        print('Parent of Parent of A')

class ParentOfParentOfB:
    def parentMethod(self):
        print('Parent of Parent of B')

class ParentOfA(ParentOfParentOfA):
    def parentMethod1(self):
        print("Parent of A")

class ParentOfB(ParentOfParentOfB):
    def parentMethod(self):
        print("Parent of B")

class A(ParentOfA):

    def methodA(self):
        print("MethodA")

    def method_overriden(self):
        print('overridden from Class A')


class B(ParentOfB):
    def methodB(self):
        print("MethodB")

    def method_overriden(self):
        print('overriding in from Class B')


class C(A, B):
    def method_overriden1(self):
        print('overriding in from Class C')



c = C()
c.method_overriden()
c.parentMethod()
'''
It will first check if the method is in 'C' then it will check in 'A' and 'B' and 'object' in that order
The order in which they are present in the overridden method.
'''
#print(C.__mro__)  # prints the method resolution order.
