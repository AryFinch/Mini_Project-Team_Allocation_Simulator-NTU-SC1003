# ⚠️机密 文件:核心算法

#import
from student import Student
from team import Team

class TeamAllocator:
    """
    """
    
    def __init__(self,original_students:list[Student]):
        # copy data
        from copy import deepcopy
        self.students_copy=deepcopy(original_students);

        #set data
        self.teams=list();
        self.unallocated_students=list();
        
        #log the basic diversity or equality of the whole students
        all_in_team=Team(self.students_copy);
        self.overall_gender_rate=all_in_team.gender_rate;
        self.overall_school_diversity=all_in_team.school_diversity;
        self.overall_cgpa_average=all_in_team.cgpa_average;
    
        pass;
    
    def _list_teams_not_full(self,team_capacity) -> list[Team]:
        ans=[]
        for team in self.teams:
            if len(team.students)<team_capacity:
                ans.append(team);
        return ans;
    
    def _break_team_into_unallocated_students(self,team_index):
        for student in self.teams[team_index].students:
            self.unallocated_students.append(student);
        del self.teams[team_index];
        pass;
    
    def _assign_unallocated_student_to_team(self,team_capacity):
        """
        检查unallocated_students
        如果存在team,将它分到合适的team中
        如果没有,创建一个team
        """
        # pull-out the first one to assign
        while len(self.unallocated_students):
            #get the first student to allocate
            student=self.unallocated_students.pop(0);

            # rigister the best choice
            best_team=Team([]); 
            best_score=int(-2147483647);

            # get list of teams need student
            teams_need_students= self._list_teams_not_full(team_capacity);
            for new_team in teams_need_students:

                # forsee if the allocation is reasonable
                team_if_add_student=Team(new_team.students+[student])
                new_score=team_if_add_student.estimate_diversity_of_team(self.overall_gender_rate,self.overall_school_diversity,self.overall_cgpa_average) # estimate the score if the student join
                
                #to compare all the ways of allocating and keep the best one
                if new_score>best_score:
                    best_score=new_score;# record the best choice
                    best_team=new_team;
            
            # finally add the student into the best team
            best_team.add_student(student);
            
            # if no existed team is chosen
            if len(best_team.students)==1:# this mean that the best choice is the empty one, indicating that teams is empty
                self.teams.append(best_team);
                pass;

        pass;
    
    def tag_students_with_teams(self,students:list[Student]):
        for original_student in students:
            have_found=False;
            for team_index in range(len(self.teams)):
                for teamed_student in self.teams[team_index].students:
                    if original_student.name==teamed_student.name:
                        original_student.team_assigned=str(team_index);
                        # print(original_student.string_form);
                        have_found=True;
            if have_found!=True:
                return 0;
        
        return 1;

    def begin(self,team_capacity:int):
        """
        传入:列表(Student);一个组的人数

        对于要组成X个人的team,将第X个人加入已有X-1个人的组.
        第X个人来自被拆散的组,将最不符合“要求”的组拆散
        """
        
        # basic statement
        if team_capacity==1:
            # erase data
            self.unallocated_students=[];
            self.teams=[];

            # pull all students into unallocated_students
            from copy import deepcopy
            self.unallocated_students=deepcopy(self.students_copy);

            # assign all unall. into teams of itself
            self._assign_unallocated_student_to_team(team_capacity);
            pass;
        
        # advanced statements
        elif team_capacity>1:
            # get the team allocation with 1 less students
            self.begin(team_capacity-1);
            
            # rank the already-existed teams by overall score
            self.teams.sort();# leave for further investigation
            
            # choose the bad team, break and pull into unallo.
            while len(self._list_teams_not_full(team_capacity))>1:# if there is unfinished team
                if len(self.teams):
                    self._break_team_into_unallocated_students(0);# this is the worst team

            # assign students in unallo. into teams need a student
            self._assign_unallocated_student_to_team(team_capacity);

            pass;
        else:
            raise ValueError;
    
        # self._tag_students_with_teams();
    
        pass;
    
    # def estimate_diversity_of_team(self,original_team:Team):
    #     """
    #     传入:Team
    #     传出:int该组的得分
    #     将三个维度的数据化为一个维度,衡量diversity
    #     p.s.根据要求,性别和学校多样性的权重应该较高.
    #     """
    #     pass;
    