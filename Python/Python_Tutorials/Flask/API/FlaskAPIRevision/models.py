import datetime

from peewee import *


DATABASE = SqliteDatabase('employee.db')


class Employee(Model):
    employee_id = CharField(unique=True)
    name = CharField(max_length=255)
    skills = TextField()
    experience = IntegerField()
    joined_on = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Employee], safe=True)
    # safe true does not gives error if we try to create a database that already exists
    DATABASE.close()



