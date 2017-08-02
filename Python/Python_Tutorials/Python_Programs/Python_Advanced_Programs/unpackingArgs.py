class Unpacking:
    def star(self, *args): # unpacking a list
        for arg in args:
            print('Star ' + str(arg))

    def star_start(self, **kwargs): # unpacking a dictionary.
         for value in kwargs.values():
            print( 'star_start' + str(value))

up = Unpacking()
up.star(1, 2, 3)
up.star_start(one='one', two=2, three=3)
