# ⚠️机密 文件:核心算法

#import
from student import Student
from team import Team

import logging
logging.basicConfig(
    filename="team_assigned3.csv",
    level=logging.INFO,
    format="%(message)s"
)

class TeamAllocator:
    """
    conduct core algorithms: recursion, greedy
    for N>1 Student:
        revoke self to get the allocation state of N-1
        rank(sort) teams by estimate_diversity_of_team
        break down worst team into unalloc'
        try assign unallo'd student into everyone
        choose the one with highest score after add_student
    for N=1 Student simply everyone's a Team
    """
    
    def __init__(self,original_students:list[Student]):
        """
        initialize
        """
        # copy data
        from copy import deepcopy
        self.students_copy=deepcopy(original_students);

        #set data
        self.teams=list();
        self.unallocated_students=list();
        
        #log the basic diversity or equality of the whole students
        all_in_team=Team(self.students_copy,"all_in_team");
        Team.overall_gender_rate=all_in_team.gender_rate;
        Team.overall_school_diversity=all_in_team.school_diversity;
        Team.overall_cgpa_average=all_in_team.cgpa_average;

        pass;
    
    def _list_teams_not_full(self,team_capacity:int) -> list[Team]:
        """
        I:int
        go thru teams and rec teams needing student
        O: list
        """
        ans=[]
        for team in self.teams:
            if len(team.students)<team_capacity:
                ans.append(team);
        return ans;
    
    def _break_team_into_unallocated_students(self,team_index):
        """
        I:evrything
        get the index and break corresponding team in teams
        pull students into unalloc'
        """
        # print("## _break_team_into_unallocated_students ##")
        for student in self.teams[team_index].students:
            self.unallocated_students.append(student);
        # self.teams[team_index].print();
        del self.teams[team_index];
        pass;
    
    def _assign_unallocated_student_to_team(self,team_capacity):
        """
        for everyone in unalloc':
            try add into every team_not_full, rec highest score
            if there does not exist, create one
            pull into teams
            finally add student

        检查unallocated_students
        如果存在team,将它分到合适的team中
        如果没有,创建一个team
        """
        # print("## _assign_unallocated_student_to_team ##")
        
        # pull-out the first one to assign
        while len(self.unallocated_students):
            #get the first student to allocate
            student=self.unallocated_students.pop(0);

            # rigister the best choice
            best_team=None; 
            best_score=int(-2147483647);

            # get list of teams need student
            teams_need_students= self._list_teams_not_full(team_capacity);
            for new_team in teams_need_students:

                # forsee if the allocation is reasonable
                team_if_add_student=Team(new_team.students+[student],"team_if_add_student")
                new_score=team_if_add_student.estimate_diversity_of_team # estimate the score if the student join
                
                #to compare all the ways of allocating and keep the best one
                if new_score>best_score:
                    best_score=new_score; # record the best choice
                    best_team=new_team;
            
            # print("### this is the best team:")
            # best_team.print();

            if best_team is None:
                best_team=Team([],"best_team");
                self.teams.append(best_team);
                pass;
            
            # finally add the student into the best team
            best_team.add_student(student);

            
            
            # # if no existed team is chosen
            # if len(best_team.students)==1:# this mean that the best choice is the empty one, indicating that teams is empty
            #     self.teams.append(best_team);
            #     pass;

        pass;
    
    def tag_students_with_teams(self,students:list[Student]):
        """
        tag allocation data into required format/file
        go thru required list and add corresponding data
        """
        self.print_result();
        # go trhu original list
        for original_student in students:
            # tag if found
            have_found=False;
            for team_index in range(len(self.teams)):
                for teamed_student in self.teams[team_index].students:
                    # accord with name
                    if original_student.name==teamed_student.name:
                        original_student.team_assigned=str(team_index);
                        # print(original_student.info);
                        have_found=True;
            if have_found!=True:
                print(f"have not found {original_student.info}");
                self.print();
                raise IndexError;
        
        return 1;

    def begin(self,team_capacity:int):
        """
        传入:列表(Student);一个组的人数

        conduct the procedures
        对于要组成X个人的team,将第X个人加入已有X-1个人的组.
        第X个人来自被拆散的组,将最不符合“要求”的组拆散
        """

        # basic statement
        # print(f"# begin{team_capacity}");
        
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
            
            # # rank the already-existed teams by overall score
            # self.teams.sort();# leave for further investigation
            # # self.print();
            # self.log(team_capacity);
            
            # # choose the bad team, break and pull into unallo.
            # # while len(self._list_teams_not_full(team_capacity))>1:# if there is unfinished team
            # #     if len(self.teams):
            # #         self._break_team_into_unallocated_students(0);# this is the worst team

            # # assign students in unallo. into teams need a student
            # self._assign_unallocated_student_to_team(team_capacity);

            # complete all not-full team except the last
            while len(self._list_teams_not_full(team_capacity))>1:#avoid indivisible
                # rank by sort(), cmp by estimate_diversity_of_team
                self.teams.sort();
                #
                def find_team_to_break():
                    for i in range(len(self.teams)):
                        if self.teams[i].population<team_capacity:
                            return i;
                    return -1;# to cause error
                    pass;
                #break
                self._break_team_into_unallocated_students(find_team_to_break());
                # assign
                self._assign_unallocated_student_to_team(team_capacity);
                pass;

            pass;
        else:
            # entered <1
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
    
    def print(self):
        print("unallocated students: ",end="");
        print([student.info for student in self.unallocated_students],end="");
        print("teams:",end="");
        for i in range(len(self.teams)):
            self.teams[i].print(i);
            pass;
    
    def log(self,team_capacity):
        logging.debug(":::::::::::::::::::"+f"TeamAllocator.begin({team_capacity})"+"::::::::::::::::");
        logging.debug(f"""unallocated students: {[student.info for student in self.unallocated_students]}
teams:""")
        for i in range(len(self.teams)):
            logging.debug(self.teams[i].info);
            pass;
        logging.debug("................."+f"end begin"+".................");
        pass;
    
    def print_result(self):
        logging.info(f"index,gender_rate,school_diversity,cgpa_average,*diversity")
        for i in range(len(self.teams)):
            logging.info(f"{i},{self.teams[i].gender_rate},{self.teams[i].school_diversity},{self.teams[i].cgpa_average},{self.teams[i].estimate_diversity_of_team}");
        pass;

    @property
    def info(self):
        for i in range(len(self.teams)):
            self.teams[i].index=i;
        return f"""@TeamAllocator
unallocated students: {self.unallocated_students};
teams: {[self.teams[i].info for i in range(len(self.teams))]}
""";
        pass;