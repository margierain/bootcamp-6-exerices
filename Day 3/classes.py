class Parent(object):
    
    def parent_method(self):
        print "parent yes method"
        
    def shared_method(self):
        print "shared method"
        
        
class Child(Parent):
    def parent_method(self, output_string):
        print "child yes method {}".format(output_string)
      


child = Child()
print child.parent_method("called")
child.shared_method()