from student import Student
from team import Team

class TeamAllocator:
    """
    核心:
        estimate diversity
        <DFS>
        <greedy>
    """
    
    def __init__(self,original_students:list):
        # copy data
        from copy import deepcopy
        self.students_copy=deepcopy(original_students);

        # check validity
        for i in self.students_copy:
            if not isinstance(i,Student):
                print("not student");
                raise TypeError

        #set data
        self.teams=[];
        self.unallocated_students=[];
        
        #log the basic diversity or equality of the whole students
        all_in_team=Team(self.students_copy);
        self.overall_gender_rate=all_in_team.gender_rate();
        self.overall_school_diversity=all_in_team.school_diversity();
        self.overall_cgpa_average=all_in_team.cgpa_average();
    
        pass;
    
    def _assign_unallocated_student_to_team(self,team_capa  city):
            """
            检查unallocated_students
            如果存在team,将它分到合适的team中
            如果没有,创建一个team
            """
            # pull-out the first one to assign

            # run all of the exist team and assign it to the team with highest score if it attend the team

            pass;
    
    def _break_team(self):
        pass;

    def allocate_students_into_teams(self,team_capacity:int):
        """
        传入:列表(Student);一个组的人数

        对于要组成X个人的team,将第X个人加入已有X-1个人的组.
        第X个人来自被拆散的组,将最不符合“要求”的组拆散
        """
        if team_capacity==1:
            # erase data
            self.unallocated_students=[];
            self.teams=[];
            # pull all students into unallocated_students

            # assign all unall. into teams of itself
            pass;
        elif team_capacity>1:
            # get the team allocation with 1 less students
            
            # rank the already-existed teams by overall score
            
            # choose the bad team, break and pull into unallo.

            # sort rest teams by cgpa

            # assign students in unallo. into teams need a student


            pass;
        else:
            raise ValueError;
        pass;
    
    def estimate_diversity_of_team(self,original_team:set):
        """
        传入:Team
        传出:int该组的得分
        将三个维度的数据化为一个维度,衡量diversity
        p.s.根据要求,性别和学校多样性的权重应该较高.
        """
        pass;