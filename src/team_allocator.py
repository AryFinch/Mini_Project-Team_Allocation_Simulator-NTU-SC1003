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
    
    def _break_team(self):
        pass;
    
    def _assign_unallocated_student_to_team(self,team_capacity):
        """
        检查unallocated_students
        如果存在team,将它分到合适的team中
        如果没有,创建一个team
        """
        # pull-out the first one to assign
        while len(self.unallocated_students):
            student=self.unallocated_students
            self.unallocated_students.pop(0);

        # run all of the exist team and assign it to the team with highest score if it attend the team
            best_team=Team([]); # rigister the best choice
            best_score=int(-2147483647);
            teams_need_students=[teams_need_student in self.teams if len(teams_need_student.students)<team_capacity ];
            for new_team in teams_need_students: # go thru the existed teams
                new_score=self.estimate_diversity_of_team(Team(new_team.students+[student])) # estimate the score if the student join
                if new_score>best_score:
                    best_score=new_score;# record the best choice
                    best_team=new_team;
            best_team.add_student(student);# add the student into the best team
            if len(best_team.students)==1:# this mean that the best choice is the empty one, indicating that teams is empty
                self.teams.append(best_team);
                pass;

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
            from copy import deepcopy
            self.unallocated_students=deepcopy(self.students_copy);
            self._assign_unallocated_student_to_team();

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
    
    def estimate_diversity_of_team(self,original_team:Team):
        """
        传入:Team
        传出:int该组的得分
        将三个维度的数据化为一个维度,衡量diversity
        p.s.根据要求,性别和学校多样性的权重应该较高.
        """
        pass;