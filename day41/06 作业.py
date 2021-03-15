# 基础练习 1-15
"""
1、查询男生、女生的人数；
select gender,count(gender) from student group by gender;
2、查询姓“张”的学生名单；
select * from student where sname like '张%';
3、课程平均分从高到低显示
select course_id,avg(num) from score group by course_id order by avg(num) desc;
4、查询有课程成绩小于60分的同学的学号、姓名；
    1.从score表中查询课程成绩小于60分的学号
    select student_id from score where num < 60;
    2.从student中查询sid在score中的student_id,sid
    select sid,sname from student where sid in (select student_id from score where num < 60);
5、查询至少有一门课与学号为1的同学所学课程相同的同学的学号和姓名；
    1.查询学号为1的同学所学的课程号
    select course_id from score where student_id=1;      # 1,2,4
    2.查询与学号为1的同学选着相同课程的student_id(需要去重),然后去除
    select distinct student_id from score where course_id in (select course_id from score where student_id=1);
6、查询出只选修了一门课程的全部学生的学号和姓名；
    1.从score中查找所选的课程数量为1门的student_id
    select student_id from score group by student_id having count(student_id)=1;
    2.选出student_id=13的同学的学号和姓名
    select sid,sname from student where sid in (select student_id from score group by student_id having count(student_id)=1);
7、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
    1.select course_id,max(num),min(num) from score group by course_id;
8、*****查询课程编号“2”的成绩比课程编号“1”课程低的所有同学的学号、姓名；
    1.把课程编号2的所有人的学生id,成绩找出来
    select student_id,num from score where course_id=2;
     2.把课程编号1的所有人的学生id,成绩找出来
    select student_id,num from score where course_id=1;
    3.做连表
    select * from (select student_id,num from score where course_id=1) as t1
    inner join (select student_id,num from score where course_id=1) as t2
    on t1.student_id=t2.student_id;
9、查询“生物”课程比“物理”课程成绩高的所有学生的学号；

10、查询平均成绩大于60分的同学的学号和平均成绩;

11、查询所有同学的学号、姓名、选课数、总成绩；

12、查询姓“李”的老师的个数；

13、查询没学过“张磊老师”课的同学的学号、姓名；

14、查询学过“1”并且也学过编号“2”课程的同学的学号、姓名；

15、查询学过“李平老师”所教的所有课的同学的学号、姓名；
"""

# 更多练习：
"""
1、查询没有学全所有课的同学的学号、姓名；
2、查询和“002”号的同学学习的课程完全相同的其他同学学号和姓名；
3、删除学习“叶平”老师课的SC表记录；
4、向SC表中插入一些记录，这些记录要求符合以下条件：①没有上过编号“002”课程的同学学号；②插入“002”号课程的平均成绩； 
5、按平均成绩从低到高显示所有学生的“语文”、“数学”、“英语”三门的课程成绩，按如下形式显示： 学生ID,语文,数学,英语,有效课程数,有效平均分；
6、查询各科成绩最高和最低的分：以如下形式显示：课程ID，最高分，最低分；
7、按各科平均成绩从低到高和及格率的百分数从高到低顺序；
8、查询各科成绩前三名的记录:(不考虑成绩并列情况) 
9、查询每门课程被选修的学生数；
10、查询同名同姓学生名单，并统计同名人数；
11、查询每门课程的平均成绩，结果按平均成绩升序排列，平均成绩相同时，按课程号降序排列；
12、查询平均成绩大于85的所有学生的学号、姓名和平均成绩；
13、查询课程名称为“数学”，且分数低于60的学生姓名和分数；
14、查询课程编号为003且课程成绩在80分以上的学生的学号和姓名； 
15、求选了课程的学生人数
16、查询选修“杨艳”老师所授课程的学生中，成绩最高的学生姓名及其成绩；
17、查询各个课程及相应的选修人数；
18、查询不同课程但成绩相同的学生的学号、课程号、学生成绩；
19、查询每门课程成绩最好的前两名；
20、检索至少选修两门课程的学生学号；
21、查询全部学生都选修的课程的课程号和课程名；
22、查询没学过“叶平”老师讲授的任一门课程的学生姓名；
23、查询两门以上不及格课程的同学的学号及其平均成绩；
24、检索“004”课程分数小于60，按分数降序排列的同学学号；
25、删除“002”同学的“001”课程的成绩；
"""