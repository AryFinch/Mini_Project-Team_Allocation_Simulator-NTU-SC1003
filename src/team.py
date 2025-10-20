from student import Student
class Team:
    """
    类:任意个 “Student” 组成一个Team
    students:列表,里面充满学生类
    函数:衡量该分组的性别比例,学校多样性,平均分

    """

    def __init__(self,original_students:list):
        # copy data
        from copy import deepcopy
        self.students=set();
        self.students=deepcopy(original_students);
        
        #check the content
        for student in self.students:
            if not isinstance(student,Student):
                raise TypeError;

        pass;
    
    def gender_rate(self):
        """
        输出:float性别比例
        用一种算法(是什么呢?)衡量性别比例,
        """
        pass;
    
    def school_diversity(self):
        """
        输出:float学校多样性
        学校互不重复的得分最高
        """
        pass;
    
    def cgpa_average(self):
        """
        输出:float平均cgpa
        """
        pass;
    
    pass;
