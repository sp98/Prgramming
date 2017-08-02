"""
Class Variables and Instance Variables.
"""


class Dog:
    """

    """

    color = 'red'  # class variables

    def __init__(my_self):  # works like a constructor. Called in Class initialization
        my_self.weight = 45   # instance Variables
        my_self.height = 2    # instance Variables

    def set_weight(self, weight):
        self.weight = weight

if __name__ == '__main__':
    print(Dog.color)      # accessing class variables using just the Class name
    print(Dog().height)   # accessing instance variables by creating a new object
    print(Dog().weight)
    labra = Dog()
    labra.weight = 60
    pug = Dog()
    pug.weight = 20
    print(labra.weight)
    print(pug.weight)
    print(Dog().weight)
    obese_dog = Dog()
    obese_dog.set_weight(100)
    print(obese_dog.weight)
    obese_dog.color = 'green'
    print(obese_dog.color)
    print(Dog.color)
