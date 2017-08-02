class Test:
    def __init__(self, name='Santosh', age=26, address='G11 Sec 56 Noida'):
        self.name = name
        self.age = age
        self.address = address

    def get_details(self):
        return self.name, self.address, self.age

test = Test(30, age=33) #First is a positional argument. so it will always go into name
print(test.age)
