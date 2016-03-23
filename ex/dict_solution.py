#Task one

student = {
    'name': 'An Other',
    'langs': ['Python', 'JavaScript', 'PHP'],
    'age': 23
}

def add_student(student):
    students = []
    students.append(student)
    return students

print add_student(student) 

#Task two

def oldest_student(student): 
    eldest = 0
    for stud in students:
        if eldest < stud['age']:
            eldest = stud['age']
    print(stud['name'])

   # task three
def student_lang(lang):
    for stud in students:
        if langauage in stud['langs']:
            print(stud['name'])
            return stud['name']
    
