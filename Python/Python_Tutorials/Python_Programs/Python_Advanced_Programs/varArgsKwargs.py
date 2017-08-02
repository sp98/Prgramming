class Test:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', 'Santosh')
        self.age = kwargs.get('age', 26)
        self.address = kwargs.get('address', 'G11 Sec 56 Noida')

    def get_details(self):
        return self.name, self.age, self.address


test = Test(name='Amit', age=43)
print(test.get_details())
