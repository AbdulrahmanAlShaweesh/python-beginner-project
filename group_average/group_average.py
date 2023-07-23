class StudentsAverageGroup:

    def __init__(self, students_marks):
        self.students_marks = students_marks
        # print(self.calulate_average_group())
    # calculating the average for each group

    def calulate_average_group(self):
        students = {}

        for name, marks in self.students_marks.items():
            average = 0
            for mark in marks:
                average = average + mark

            students.update({name:  average / len(marks)})
        print(students)
        return students

    def get_max_group_value(self):
        max_value = 0
        name = ''
        for names, value in self.calulate_average_group().items():
            if value > max_value:
                max_value = value
                name = names
        return max_value, name

    def get_winer_name_average(self):
        winer_value, winer_name = self.get_max_group_value()
        return f'Winer is {winer_name}, Scorted {winer_value:.2f}'

    def store_winer(self):
        winer_value, winer_name = self.get_max_group_value()
        with open(f'group_average/winer{winer_name}.txt', mode='w') as file:
            file.write(f'Winer is {winer_name} : score {winer_value:.2f}')


students_marks = {'Tom': [100, 80, 90, 65, 60, 90], 'Nader': [39, 100, 65, 90, 83, 50],
                  'James': [54, 54, 90, 89, 65, 50], 'Sarah': [84, 51, 43, 90, 50, 53],
                  'Juhn': [100, 90, 70, 55, 80, 84], 'Makel': [100, 80, 50, 65, 55, 99],
                  'Jam': [100, 65, 60, 55, 80, 83]
                  }

mechanical_class = StudentsAverageGroup(students_marks)
# print(mechanical_class.calulate_average_group())
mechanical_class.store_winer()
