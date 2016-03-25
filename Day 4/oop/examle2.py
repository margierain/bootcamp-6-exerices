class Person(object):

    def __init__(self, fname, *args, **kwargs):
        self.fname = fname

        if len(args) > 0:
            self.lname = args[0]

        if len(args) > 1:
            self.age = args[1]


        if kwargs:
            self.lname = kwargs.get('lname', '')
            self.age = kwargs.get('age', 0)




p1 = Person("John", "Adams", 21)

p2 = Person("Eva", age=41, lname="Jacobs")

print p1.fname, p1.age

print p2.fname, p2.age

