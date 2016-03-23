#Task one

student = {
    'name': 'An Other',
    'langs': ['Python', 'PHP'],
    'age': 23
}

student1 = {
    'name': 'Margaret',
    'langs': ['JavaScript', 'PHP'],
    'age': 29
}
students = []

def add_student(student):
    ''' adds students to an empty list students''' 
    
    students.append(student)
    return students

print add_student(student) 
print add_student(student1)

#Task two

def oldest_student(student): 
    ''' find the oldest student in the class  '''
    eldest = 0
    for stud in students:
        if eldest < stud['age']:
            eldest = stud['age']
    print(stud['name'])

print oldest_student(students)    

   # task three
def student_lang(lang):
    for stud in students:
        if langauage in stud['langs']:
            print(stud['name'])
            return stud['name']
    
# def oldest_student(student):
#     if len(students) == 0:
#         return " no students"
#     elif len(students) == 1:
#         return students[0]
        
#     else:
#         oldest_age = students[0]["age"]
#         oldest_student 


