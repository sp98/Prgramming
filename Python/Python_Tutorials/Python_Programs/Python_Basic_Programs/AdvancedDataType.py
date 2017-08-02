"""
Advanced data types:
1. LIST
2. DICTIONARY
"""
print ("********* LIST **********")

cars = ["Maruti" , "Honda" , "BMW"]
print (cars)
print ("*#" *20)

print (cars[0])
indian = cars[0]
foreign= cars[1]
print (indian)
print (foreign)

print ("*#" *20)

cars[0] = "Tata"
print (cars)

print ("*#" *20)

print (len(cars))
cars.append("suzuki")       # to add one item to end of list
print(cars)
cars.insert(0, "Volkswogen")   # to add item at some specific position
print (cars)

cars.extend(["car2" , "car3"])     #to add more than one item to end of list
print(cars)

del cars[5]                      # deletes an items based on its index postion in string or List
print("Deleted 5th car " + str(cars))

print("I love these cars " + ', '.join(cars))   #use join to convert a list to string like this. We can only join on list having string.

print ("*#" *20)

print (cars.index("Honda"))
cars.pop()
print(cars)
cars.remove("Tata")
print (cars)
print (cars[0:2])



print ("********* Dictionary ************")

myDict1={"Name":"Santosh" , "Age" : "26"}
print (myDict1)
print (myDict1["Name"])
print (myDict1["Age"])
myDict1["Profession"] = "SDET"
print(myDict1)
print(myDict1["Profession"])

print("*#" * 20)

employee= {'emp1':{'name': 'Santosh', 'age':26} , 'emp2' :{'name': 'Test' , 'age' : 80}}

print (employee)
print (employee['emp1'])
print (employee['emp1']['name'])

print(employee.values())
print(employee.keys())

myDict1.pop("Age")
print(myDict1)
myDict1.clear()
print (myDict1)

myDict2 = { 'name' : 'Santosh' , 'age' : 26 , 'profession' : 'Engineer'}
print (" My name is {name}. I am {age} years old and I am an {profession} by profession ".format(**myDict2))



