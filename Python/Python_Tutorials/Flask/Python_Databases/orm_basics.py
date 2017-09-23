from peewee import *

# making a sqlite collection
db = SqliteDatabase('students.db') # the name of the database


class Student(Model):
    # models class name should be singular
    # var char field.
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0) # use default value if no value is present.

    # creating a class to show which database should be used.
    # we can provide other things like default ordering in this class as wel.
    class Meta:
        database = db


students = [
    {'username': 'student4',
     'points' : 122},
    {'username': 'student5',
     'points' : 142},
    {'username': 'student6',
     'points' : 129},
]


def add_students():
    for student in students:
        try:
            Student.create(username=student['username'],
                           points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username']) # fetch the student record.
            student_record.points = student['points'] # update the points.
            student_record.save()  # save the updated record.


def top_student():
    student = Student.select().order_by(Student.points.desc).get()
    # sort the Students table by point and get the first instance using get method.
    return student


if __name__ == '__main__':
    db.connect() # connecting to the database.
    db.create_tables( [Student], safe=True)
    # safe = true allows us to run it multiple times.
    #  And it won't fail if the database is already created
    add_students()
    print('our top student is {0.username}'.format(top_student()))


