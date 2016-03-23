from inheritance import Parent

class Child(Parent):
# to over you need to use the same function name
    ''' learning on how to overide the parent class '''
    def parent_method(self, output_string):
        print "child yes method {}".format(output_string)
      


child = Child()
print child.parent_method("called")
child.shared_method()

#print dir(Parent())
print Parent().parent_method()
