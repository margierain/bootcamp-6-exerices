def say_my_name():
    ''' use a method called format to create place holders for actual inputs'''
    print "My name is {}".format(name)

#call the function 
nam = say_my_name('margaret')  
print nam


def sum_num(num1,num2):
    total = num1 + num2
    return total

print sum_num(2,5)    