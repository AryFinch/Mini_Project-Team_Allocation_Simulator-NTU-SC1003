from student import Student
class Team:
    """
    类:五个 “Student instances” 组成一个Team
    常量:
        CAPACITY:一个team能够容纳多少student在列表students里面
    students:列表,里面充满学生类
    """
    CAPACITY=5;

    def __init__(self,original_students:list):
        #copy the list
        from copy import deepcopy
        self.students=deepcopy(original_students);

        #check capacity
        if len(self.students)>self.CAPACITY:
            raise TypeError;
        
        #check the content
        for student in self.students:
            if not isinstance(student,Student):
                raise TypeError;

        pass;
    
    pass;
