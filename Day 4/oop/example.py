class Animal(object):
    ''' animal _count is a class property '''

    animal_count = 0
    
    def __init__(self, name):
        self.name = name
        Animal.animal_count += 1
        self.id = Animal.animal_count

    def eat(self):
        return "yes, I eat :)"

class Cat(Animal):

    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.legs = 4

    def walk(self):
        return "I walk with {0} legs".format(self.legs)



my_cat = Cat("wafula")

print my_cat.eat()
print my_cat.walk()
print my_cat.name, ", ID#", my_cat.id

another_cat = Cat("paka")
print another_cat.name, ", ID#", another_cat.id
