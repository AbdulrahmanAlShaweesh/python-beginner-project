class AverageMarksCalculator : 
    
    def __init__(self, marks) :
        self.marks = marks 
    
    def calculat_marks(self) :
        student_average_marks = {}
        
        for name, marks in self.marks.items() :
            # calcualt the average for each students. 
            total_marks = 0 
            average = 0
            for mark in marks : 
                total_marks += mark
                average =  total_marks / len(marks)
            # print(name)
            student_average_marks.update({name : round(average, 2)}) 
        return student_average_marks 
    
    def student_average_marks(self) : 
        return self.calculat_marks()
    
    def store_stuent_average(self) : 
        with open('studentMarks/average.txt', mode='w') as f : 
            f.write('name \t\taverage\n')
            f.write('**************************\n')
            for name, average in self.calculat_marks().items() :
                f.write(f'{name} : \t {average}\n')
             

student_test = {
    'Annie': [85, 90, 75], 
     'Binnie': [ 82, 98, 80], 
    'Carol': [83, 86, 91], 
    'Daris': [89, 90, 76],
    }
studetn_1 = AverageMarksCalculator(student_test)
print(studetn_1.student_average_marks())
studetn_1.store_stuent_average()