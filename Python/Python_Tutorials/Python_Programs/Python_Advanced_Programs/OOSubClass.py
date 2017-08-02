class Student:
    name = 'All Students'
    age = 30
    roll_number = 40

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return '{} has a name {}, age {} and roll_number is {}'.format(self.__class__.__name__,
                                                                 self.name, self.age, self.roll_number
                                                                 )

class Mahesh(Student):
    name = 'Mahesh'
    age = 12
    roll_number = 33


class Suresh(Student):
    name = 'Suresh'
    age = 13
    roll_number = 50
