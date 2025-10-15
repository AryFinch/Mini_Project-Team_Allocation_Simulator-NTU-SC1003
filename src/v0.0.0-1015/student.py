class Student:
    ##############################################
    #

    #
    def __init__(self,tutorial_group="",student_id="",name="",school="",gender="",cgpa=""):
        from copy import deepcopy
        self.tutorial_group=deepcopy(tutorial_group)
        self.student_id=deepcopy(student_id);
        self.name=deepcopy(name)
        self.school=deepcopy(school)
        self.gender=deepcopy(gender)
        self.cgpa=deepcopy(cgpa);
    pass;