from team_allocator import TeamAllocator
from student import Student
from team import Team

class TeamAllocationSimulator:
    def __init__(self):
        self.file_address="";
        pass;

    def _parse_lines_from_csv_file(self,original_csv_file):
        pass;

    def _parse_students_from_lines(self,original_lines):
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
        team_allocator=TeamAllocator();
        teams=TeamAllocator.

        # turn list into csv file:

        # cover old with new one:

        pass;
    pass;