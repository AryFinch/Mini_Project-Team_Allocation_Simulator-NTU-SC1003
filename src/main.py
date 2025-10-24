"""
Team_Allocation_Simulator:main.py
Author:...
所有程序从这里开始,调用写好的TeamAllocationSimulator创建实例,使用方法begin()开始
"""

#常量定义
FILE_ADDRESS="records.csv";

#标准库

#创建实例
from simulator import TeamAllocationSimulator
team_allocation_simulator=TeamAllocationSimulator(FILE_ADDRESS);

#运行
if True:
    team_allocation_simulator.begin();