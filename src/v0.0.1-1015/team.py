from student import Student
class Team:
    ##############################################
    #

    #
    CAPACITY=5;

    def __init__(self,original_students:list):
        from copy import deepcopy
        students_copy=deepcopy(original_students);
        if len(students_copy)>self.CAPACITY:
            pass;#tbc invalid
        pass;
    
    pass;
