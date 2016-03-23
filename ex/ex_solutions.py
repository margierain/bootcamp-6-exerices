# 1. Array Reverse

def reverse(text):
    num=len(text)-1
    string=[]
    for x in text:
        while num >= 0: 
            string.append(text[num])
            num -= 1
    return "".join(string)
# call the function    
print reverse("abcd")

# 2. Equilibrium



#3.Number to words
numbers = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5':'five', '6':'six', '7': 'seven', '8': 'eight', '9': 'nine'}

def num_to_words(number):
    number = str(number)
    string =''
    for digit in number:
        string += numbers[digit] + ", "
    return string 
# call the function
print num_to_words(345657)

#4.Factorial
def factorial(n):
    if n = 0:
        return 1
    else:
        return n * factorial(n -1) 

# call th function
print factorial(4)        

#5.Sum of Digits 
mylist = [10,34,56,89]

def sum_of_digits(lst):
    total = 0
    new_list = []
    for a in lst:
        new_list += list(str(a))
    for number in new_list:    
        total += int(number)
    return total

# call the function
print sum_of_digits(mylist) 

#6.Sum of Unique Digits   
def sum_of_unique_nums(A):
    total = 0
    new_set = set(A)
    for number in new_set:    
        total += int(number)
    return total


# call the function
print sum_of_unique_digits([2,4,4,2])    