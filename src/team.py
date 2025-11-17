from student import Student
class Team:# 类 概念
    """
    class stores many Student into students:list
    include function calculate its 3 properties + population
    include function estimate diversity, turn 3 dimensions into 1 number by weighted average

    类:任意个 “Student” 组成一个Team
    students:列表,里面充满学生类
    函数:衡量该分组的性别比例,学校多样性,平均分

    """
    # initialize the overall data, for estimate diversity
    overall_gender_rate:float=1.0;
    overall_school_diversity:float=1.0;
    overall_cgpa_average:float=4.0

    def __init__(self,original_students:list[Student],index):
        # copy data
        from copy import deepcopy
        self.students=list();
        self.students=deepcopy(original_students);

        self.index=index;
        
        #check the content
        for student in self.students:
            if not isinstance(student,Student):
                raise TypeError;
        
        pass;
    
    @property
    def gender_rate(self):
        """
        输出:float性别比例
        count gender in the dictionary
        output Male/Female (both≠0); 0 (either=0)
        """
        count_types={"Male":0,"Female":0};
        for student in self.students:
            if not student.gender in count_types:# if appear wrong data or something else
                raise TypeError;
                # count_types[student.gender]=0;
            count_types[student.gender]+=1;
        
        #evaluate the diversity.
        # for value in list(count_types.values):
        if count_types["Female"]*count_types["Male"]==0:### there is a problem!!
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
        len of set / len of list simply
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
            return 0;# shall let it report error actually
        pass;
    
    @property
    def cgpa_average(self):
        """
        输出:float平均cgpa
        average
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
    
    @property
    # def estimate_diversity_of_team(self,overall_gender_rate,overall_school_diversity, overall_cgpa_average):
    def estimate_diversity_of_team(self):
        """
        传出:int该组的得分
        weighted average
        将三个维度的数据化为一个维度,衡量diversity
        p.s.根据要求,性别和学校多样性的权重应该较高.
        """
        WEIGHT_GENDER_RATE=0.7;
        WEIGHT_SCHOOL_DIVERSITY=0.2;
        WEIGHT_CGPA_AVERAGE=0.1;
        
        return self.gender_rate/Team.overall_gender_rate*WEIGHT_GENDER_RATE+self.school_diversity/Team.overall_school_diversity*WEIGHT_SCHOOL_DIVERSITY+(1-abs(self.cgpa_average-Team.overall_cgpa_average))*WEIGHT_CGPA_AVERAGE;
        

        # return self.gender_rate*WEIGHT_GENDER_RATE+self.school_diversity*WEIGHT_SCHOOL_DIVERSITY+self.cgpa_average*WEIGHT_CGPA_AVERAGE;

        pass;
    
    # def __gt__(self,other):
    #     return self.estimate_diversity_of_team>other.estimate_diversity_of_team;

    def __lt__(self,other):
        """
        O:bool diversity comparison
        for sort function convenience
        """
        return self.estimate_diversity_of_team<other.estimate_diversity_of_team;

    pass;

    @property
    def population(self):
        """
        len of students
        """
        return len(self.students);

    def print(self,index="Unknown"):
        print(f"""
### team {index}###
diversity = {self.estimate_diversity_of_team};
gender_rate = {self.gender_rate};school_diversity = {self.school_diversity};cgpa_avg = {self.cgpa_average};
students:{[f"{student.info}" for student in self.students]};
""");

    @property
    def info(self):
        return f"""
@ team {self.index} of {self.population}
diversity = {self.estimate_diversity_of_team};
gender_rate = {self.gender_rate};school_diversity = {self.school_diversity};cgpa_avg = {self.cgpa_average};
students:{[f"{student.info}\n" for student in self.students]};
"""
        pass;