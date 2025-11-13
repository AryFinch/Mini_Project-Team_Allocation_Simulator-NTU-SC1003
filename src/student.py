class Student:
    """
    Present all the information of a student
    Include str:
    tutorial_group,student_id,name,school,gender,cgpa
    
    一个学生的所有信息
    包括str:
    tutorial_group,student_id,name,school,gender,cgpa
    """
    def __init__(self,tutorial_group="",student_id="",school="",name="",gender="",cgpa:float=0.0):
        """
        初始化函数,
        传入:str / float
        将自己的各种数据按照参数一一赋值
        """
        #深拷贝,养成意识
        from copy import deepcopy
        self.tutorial_group=deepcopy(tutorial_group)
        self.student_id=deepcopy(student_id);
        self.name=deepcopy(name)
        self.school=deepcopy(school)
        self.gender=deepcopy(gender)
        self.cgpa=deepcopy(cgpa);
        # prevent bad data
        try:
            self.cgpa = float(cgpa)
        except:
            self.cgpa = 0.0
        # might not be used, but leave the possibility.
        self.team_assigned=deepcopy(str());
    pass;

    @property
    def info(self):
        return f"{self.tutorial_group},{self.student_id},{self.school},{self.name},{self.gender},{self.cgpa},{self.team_assigned}"
