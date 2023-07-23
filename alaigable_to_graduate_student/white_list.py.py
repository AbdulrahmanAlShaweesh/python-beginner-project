

def gratuateStudentsList(blackListStudents, whiteListStudent, studentsList, totalStudents):

    try:
        for i in range(int(totalStudents)):

            name = input('studetn\'s name ? ').strip().lower()
            while name == '':
                name = input(
                    'Do\'nt enter an empty studetn\'s name ? ').strip().lower()
            studentsList.append(name)
    except:
        print('error occurs.')

    for student in studentsList:
        if student not in blackListStudents:
            whiteListStudent.append(student.title())
    print(
        f'the total graduating students {len(whiteListStudent)} {"are" if len(whiteListStudent) > 1 else "is"} {"studetns" if len(whiteListStudent) > 1 else "studetn"}')

    with open('alaigable_to_graduate_student/sudent_allowed_to_graduate.txt', 'a') as file:
        for student in whiteListStudent:
            file.write(f'Name : {student}\n')
    with open('alaigable_to_graduate_student/sudent_allowed_to_graduate.txt', 'r') as file:
        # for student in :
        print(file.readlines())

    print(sorted(whiteListStudent), sep='\n')


blackListStudents = ['sara', 'sager', 'tom']
whiteListStudent = []
studentsList = []
totalStudents = input('enter the number of studetns ? ').strip()

gratuateStudentsList(blackListStudents, whiteListStudent,
                     studentsList, totalStudents)
