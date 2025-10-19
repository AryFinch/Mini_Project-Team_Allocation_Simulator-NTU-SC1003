# ⚠️机密 文件:核心算法

#import
from student import Student
from team import Team

class TeamAllocator:
    """
    核心:
        estimate diversity
        <DFS>
        <greedy>
    """
    def __init__(self):
        pass;
    
    def estimate_diversity_of_team(self,original_team:Team):
        """
        传入:Team
        传出:int该组的得分
        将三个维度的数据化为一个维度,衡量diversity
        """
        pass;

    def allocate_students_into_teams(self,original_students,team_capacity):
        """
        传入:列表(Student);一个组的人数

        递归,对于要组成X个人的team,将第X个人加入已有X-1个人的组.
        第X个人来自被拆散的组,将最不符合“要求”的组拆散
        """
        # copy data
        from copy import deepcopy
        students=deepcopy(original_students);

        # basic state
        if team_capacity==1:
            return Team(students);
    
        #

        pass;