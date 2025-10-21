#导入其他文件类
from team_allocator import TeamAllocator
from student import Student
from team import Team

class TeamAllocationSimulator:
    def __init__(self,file_address=""):
        """
        TeamAllocationSimulator初始化
        """
        self.file_address=file_address;
        self.TEAM_CAPACITY=5;
        pass;

    def _parse_lines_from_csv_file(self,original_csv_file):
        """
        传入:源文件,不是地址
        传出:列表
        源文件每一行作为列表lines的每一项
        *无视第一行*
        """
        pass;

    def _parse_students_from_lines(self,original_lines):
        """
        传入:列表 源文件的各个行
        传出:列表(student类)
        将lines的每一项化成student
        """
        pass;
    
    # def _parse_teams_into_csv_file(self,original_teams):
    #     """
    #     传入:列表(team类)
    #     传出:
    #     """
    #     pass;
    
    def _modify_lines_from_teams(self,original_lines,original_teams):
        """
        传入:列表 源文件的每一列; 列表 team
        传出:列表 输出文件的每一列
        遍历源文件的每一列,将该列学生所分组按照teams添加新的一列
        """
        pass;

    def begin(self):
        # open file:
        lines=[];
        try:
            with open(self.file_address,'r') as csv_file:
                
        # process file to lines:
                lines=self._parse_lines_from_csv_file(csv_file);
                
        except:
            pass;# tbc invalid
        
        # process sheet to student list:
        students=self._parse_students_from_lines(lines);
        
        # call allocator parse team list:
        team_allocator=TeamAllocator(students);
        teams=team_allocator.allocate_students_into_teams(self.TEAM_CAPACITY);

        # turn list into csv file:
        new_lines=self._modify_lines_from_teams(lines,teams);

        # create file and put answer in
        try:
            with open("out2.csv",'w') as out_file:
                for i in new_lines:
                    print(i,file=out_file);
            pass;
        except:
            pass;#tbc error
        pass;
    pass;