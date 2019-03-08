from collections import defaultdict 

class School:
    def __init__(self, name, student_name=None, student_grade=None):
        self.name = name
        self.student_name = student_name
        self.student_grade = student_grade
    
    roster_dict = {}

    def roster(self):
        return self.roster_dict

    def add_student(self,s_name,s_grade):
        self.student_name = str(s_name)
        self.student_grade = s_grade
        
        student_list = []
        student_tuple = (self.student_grade, self.student_name)
        student_list.append(student_tuple)
        student_dict = defaultdict(list)

        for self.student_grade, self.student_name in student_list:
            student_dict[self.student_grade].append(self.student_name)
    
        self.roster_dict.update(student_dict)
    
    def grade(self, key):
        return self.roster_dict[key]

        