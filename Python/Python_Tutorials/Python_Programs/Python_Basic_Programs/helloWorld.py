print ('Hello World!')
print ('Python program in Pycharm is awesome!')

print ("****************")
for x in range(0, 100):
    print (x)

print ("****************")

print (bool(""))
print (bool("Santosh"))

print ("****************")

print ("Something in \"quotes\" ")
print ("someting in \
new line")

print ("****************")

someText = "Santosh"
print (someText[0])
print (someText[5])
#print(someText[10])


print ("****************")
text1 = "Santosh"
print (len(text1))
print (text1.lower())
print (text1.upper())


print ("****************")
text2 = "Santosh PILLAI"
print (text2[0:8])
print (text2[0:8:2])
print(text2[5:])
print(text2[::-1])


print ("****************")
text3 = "SantoshPILLAI2"

dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"


def string_factory(list_of_dicts, my_string):
    returned_list = []
    for single_dicts in list_of_dicts:
        returned_list.append(my_string.format(**single_dicts))

    return returned_list

print (string_factory(dicts, string) )


teacher_dict = {'Jason Seifer': ['Ruby Foundations', 'Ruby on Rails Forms', 'Technology Foundations'],'Kenneth Love': ['Python Basics', 'Python Collections']}


def most_classes(teacher_dict):
    max_count = 0;
    max_count_teacher = ""
    for teachers in teacher_dict:
        if len(teacher_dict[teachers]) > max_count:
            max_count = len(teacher_dict[teachers])
            max_count_teacher = teachers

    return max_count_teacher


def num_teachers(teacher_dict):
    total_teachers = 0;
    for teacher in teacher_dict:
        total_teachers = total_teachers + 1

    return total_teachers


def stats(teacher_dict):
    list_of_list = []
    for teachers in teacher_dict:
        list_of_list.append([teachers, len(teacher_dict[teachers])])

    return list_of_list


def courses(teacher_dict):
    available_courses = []
    for taught_courses in teacher_dict.values():
        for each_course in taught_courses:
            available_courses.append(each_course)

    return available_courses



def stringcases(my_string):
    return my_string.lower(), my_string.upper(), my_string.title(), my_string[::-1]



for index, value in enumerate(range(1, 100)):
    print("{}  {}".format(index+1, value))

for data in enumerate(range(1, 100)):
    print("{}  {}".format(data[0]+1, data[1]))

for data in enumerate(range(1, 100)):
    print("{}  {}".format(*data))

itr1 = [1, 2, 3]
itr2 = [3, 4, 5]

def combo(itr1, itr2):
    tuple_list = []
    for data1, data2 in zip(itr1, itr2):
        tuple_list.append((data1, data2))

    return tuple_list

print("This teacher has most classes -  " + most_classes(teacher_dict))
print("There are a total of {} teachers".format(num_teachers(teacher_dict)))
print(stats(teacher_dict))
print(courses(teacher_dict))
print(stringcases("santosh is back"))

print(combo(itr1, itr2))

