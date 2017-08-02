class DefaultArgs:
    def method1(self, age=10, name='Santosh'):
        print(name)
        print(int(age))

if __name__ == '__main__':
    d = DefaultArgs()
    d.method1()
    d.method1(26, 'Santosh')
    d.method1(10, 'sasdf')
