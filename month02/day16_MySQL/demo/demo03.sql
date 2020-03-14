--view(表的映射的虚拟表)
create view good_stu as select name,age,sex,score from cls where score > 85;
insert into good_stu values(6,'www',18,'w',93);

--查看所有视图
show full tables in student where table_type like 'VIEW';

drop view if exists c5;
alter view  c1 as select name,age,score from class_1;