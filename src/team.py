from student import Student
class Team:
    """
    类:任意个 “Student instances” 组成一个Team
    常量:
        CAPACITY:一个team能够容纳多少student在列表students里面
    students:列表,里面充满学生类
    """

    def __init__(self,original_students:list):
        from copy import deepcopy
        self.students=set();
        self.students=deepcopy(original_students);
        
        #check the content
        for student in self.students:
            if not isinstance(student,Student):
                raise TypeError;

        pass;
    
    def gender_rate(self):
        pass;
    
    def school_diversity(self):
        pass;
    
    def gpa_average(self):
        pass;
    
    pass;
