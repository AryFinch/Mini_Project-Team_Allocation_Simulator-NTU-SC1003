from student import Student
class Team:# 类 概念
    """
    类:任意个 “Student” 组成一个Team
    students:列表,里面充满学生类
    函数:衡量该分组的性别比例,学校多样性,平均分

    """

    def __init__(self,original_students:list[Student]):
        # copy data
        from copy import deepcopy
        self.students=list();
        self.students=deepcopy(original_students);
        
        #check the content
        for student in self.students:
            if not isinstance(student,Student):
                raise TypeError;
        
        pass;
    
    @property
    def gender_rate(self):
        """
        输出:float性别比例
        用一种算法(是什么呢?)衡量性别比例,
        """
        count_types={"Male":0,"Female":0};
        for student in self.students:
            if not student.gender in count_types:# if appear wrong data or something else
                count_types[student.gender]=0;
            count_types[student.gender]+=1;
        
        #evaluate the diversity.
        # for value in list(count_types.values):
        if count_types["Female"]*count_types["Female"]==0:
            return 0; #lack one pass all

        numerator=min(count_types["Female"],count_types["Male"]);
        denominator=max(count_types["Female"],count_types["Male"]);

        return numerator/denominator;
        
        pass;
    
    @property
    def school_diversity(self):
        """
        输出:float学校多样性
        学校互不重复的得分最高
        """
        count_types={};
        for student in self.students:
            if not student.school in count_types:# if appear wrong data or something else
                count_types[student.school]=0;
            count_types[student.school]+=1;
        
        # evaluate
        try:
            return len(count_types)/len(self.students);
        except ZeroDivisionError:
            return 0;
        pass;
    
    @property
    def cgpa_average(self):
        """
        输出:float平均cgpa
        """
        sum=0;
        for student in self.students:
            sum+=student.cgpa;
        try:
            return sum/len(self.students);
        except ZeroDivisionError:
            return 0;
        pass;
    
    def add_student(self,new_student:Student):
        self.students.append(new_student);
    

    def estimate_diversity_of_team(self,overall_gender_rate:float,overall_school_diversity:float,overall_cgpa_average:float):
        """
        传入:3 overalls
        传出:int该组的得分
        将三个维度的数据化为一个维度,衡量diversity
        p.s.根据要求,性别和学校多样性的权重应该较高.
        """
        WEIGHT_GENDER_RATE=0.5;
        WEIGHT_SCHOOL_DIVERSITY=0.3;
        WEIGHT_CGPA_AVERAGE=0.2;

        return self.gender_rate/overall_gender_rate*WEIGHT_GENDER_RATE+self.school_diversity/overall_school_diversity*WEIGHT_SCHOOL_DIVERSITY+self.cgpa_average/overall_cgpa_average*WEIGHT_CGPA_AVERAGE;

        pass;
    
    # def __gt__(self,other):
    #     return self.estimate_diversity_of_team>other.estimate_diversity_of_team;

    def __lt__(self,other):
        return self.estimate_diversity_of_team<other.estimate_diversity_of_team;

    pass;
