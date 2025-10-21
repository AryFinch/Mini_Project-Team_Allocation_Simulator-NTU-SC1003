# Mini_Project-Team_Allocation_Simulator-NTU-SC1003

Li Zhuochen
*21/10/25*

# 项目流程 🎯
- [x] 1. 设计程序结构
- [ ] 2. 填写写主干内容
- [ ] 3. 调试至无明显bug

- [ ] 1. 写“可视化”部分
- [ ] 2. 迁移至Jupyter notebook
- [ ] 3. 填写展示文字markdown
- [ ] 4. 调试至无明显bug

- [ ] 1. 准备展示稿件
- [ ] 2. 提交文件
- [ ]    1. 名字,requirement.txt,zip
- [ ] 3. make an appointment
- [ ] 4. final

## 待完成函数
### team.py
- [ ] gender_rate
- [ ] school_diversity
- [ ] cgpa_average
### simulator.py
- [ ] _parse_lines_from_csv_file
- [ ] _parse_students_from_lines
- [ ] _modify_lines_from_teams
### team_allocator.py
- [ ] _assign_unallocated_student_to_team
- [ ] _break_team
- [ ] estimate_diversity_of_team
- [ ] (Li Zhuochen) allocate_students_into_teams
- [ ] (Li Zhuochen) allocate_students_into_teams
- [ ] (need design) estimate_diversity_of_team

## stucture 🏛️
**student.py**:封装了一个学生的所有信息

**team.py**:一个学生的列表,同时附加一些计算组内的基本信息

**main.py**程序的门户,声明一个“simulator”实例,调用它对数据进行处理. main本身没有做任何事

**simulator.py**包括整个程序的主要顺序,从文件读入,分组到输出

**team_allocator.py**负责核心算法

## 合作教程 🤹
*以下同时介绍如何使用github并介绍**面向对象***
```py
class CooperationTutorial:
    def __init__(self):
        """
        每当你开始进行一个*实际*的教程时,就要执行我
        """
        pass;

    def begin(self):
        self.打开GitHub官网("https://github.com");
        self.注册账户();

        self.下载GitHub("https://desktop.github.com/download/");
        self.安装——打开——登陆();
        self.创建(Tutorial_Repository);
        self.完成Tutorial();
        print("现在你应该对如何管理和合作进行一个项目有所了解了")

        mini_project=self.加入Project(找人="Li Zhuochen");
        mini_project.clone(location="你的电脑任意位置")
        mini_project.create_branch();# 创建一个你的分支,你的修改会在你的分支上
        while True:
            you.写代码(mini_project);
            if is_所有任务完成():
                mini_project.commit();# 在左下角,同时写清楚主要进展:对什么文件修改/添加了什么......
                mini_project.push();

            if is_finish_branch():
                mini_project.merge();#注意⚠️ 一定要确保正确,没有冲突

    def 没有用的函数():
        """
        这个函数几乎没有什么用,为什么呢?
        """
        pass;

    def 打开GitHub官网(self,address:str):
        """
        在上面__init__()中要用到的函数,比如说我,就要定义在“合作教程里面”
        输入:str address
        address被限定为str
        """
        ...;

    def 注册账户(self):
        """
        为什么这两个函数都有一个self作为参数,在调用的时候却并没有在括号里写一个东西?
        其实self跑到了函数前面去!两者用了‘.’连接起来
        那么
            self.注册账户()
        的意思有点像我(也就是self)去 注册账户
        """
        ...;

    ...;# 剩下的省略

# class的外面......
tutorial = CooperationTutorial();
tutorial.begin();

```
怎么理解这两句话?
想象另一个场景:
```
from stationary_store import Pencil
my_pencil=Pencil();
```
这个就好像,你要去文具店买笔,最开始你只有‘笔’这一个 概念(也就是类(class) )
当你买到笔了,my_pencil就是Pencil的一个实例(instance);
区别: Pencil无法做任何事情,my_pencil才能够写字!
因为Pencil是’虚无缥缈‘的概念(类),而笔才是”真的“实例!

所以,这两句话的意思是:
我创建了一个tutorial实例;
我的tutorial开始啦;
