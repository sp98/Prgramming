class Parent:
    __parentVar = 'Test' # a private variable with __

    def __init__(self):
        print('Parent instance Created')

    def parent_specific_method(self):
        print("This is a parent specific method")


class Child1(Parent):
    child1_var = "Test2"

    def __init__(self):
        print('Child Instance created')

    def child1_specific_method(self):
        print("This is a child 1 specific method")


class GrandChild(Child1):
    grand_child_var = 'Test3'

    def __init__(self):
        print("Grand Child instnace Created")

    def grand_child_specific_method(self):
        print('This is a Grand Child Specific Method')

    def overridden_method(self):
        print("Overridden Method from teh Grand Child class")


class AdoptedClass(GrandChild, Child1):
    adopted_var = "Test4"

    def __init__(self):
        print("Adopted Child instnace Created")

    def adopted_specific_method(self):
        print('This is an adopted specifice method')

    def overridden_method(self):
        print('Overridden method from the adopted class')


if __name__ == '__main__':
    grand_child = GrandChild()
    grand_child.parent_specific_method()
    grand_child.child1_specific_method()
    grand_child.grand_child_specific_method()

    adopted = AdoptedClass()
    adopted.adopted_specific_method()
    adopted.overridden_method()
    grand_child.overridden_method()

    parent = Parent()
    print(parent._Parent__parentVar)
    print(parent.__parentVar)
