class Student:
    """
    一个学生的所有信息
    包括str:
    tutorial_group,student_id,name,school,gender,cgpa
    """
    def __init__(self,tutorial_group="",student_id="",name="",school="",gender="",cgpa=""):
        from copy import deepcopy
        self.tutorial_group=deepcopy(tutorial_group)
        self.student_id=deepcopy(student_id);
        self.name=deepcopy(name)
        self.school=deepcopy(school)
        self.gender=deepcopy(gender)
        self.cgpa=deepcopy(cgpa);
    pass;