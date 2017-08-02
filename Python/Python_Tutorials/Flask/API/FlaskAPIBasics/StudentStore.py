import pymongo
from pymongo import MongoClient, errors


def store_student_info(info):
    client = MongoClient()
    db = client.StudentDB.StudInfo
    db.insert(info)
    client.close()


def get_student_info(id=0):
    student_info = []
    client = MongoClient()
    db = client.StudentDB.StudInfo
    print(id)
    if id != 0:
        student_data = db.find({'id': id}, {'_id': False})
        for data in student_data:
            student_info.append(data)
    else:
        student_data = db.find({}, {'_id': False})
        for data in student_data:
            student_info.append(data)

    if len(student_info) == 0:
        message = "No student with id " + str(id)
        student_info.append({"message" : message})

    return student_info


def delete_student_info(id=0):
    client = MongoClient()
    db = client.StudentDB.StudInfo
    if id != 0:
        db.remove({'id': id})
    else:
        db.remove({})

    client.close()












