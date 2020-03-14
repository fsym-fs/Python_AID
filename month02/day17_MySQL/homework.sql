+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int(11)      | NO   | PRI | NULL    | auto_increment |
| title        | varchar(30)  | NO   |     | NULL    |                |
| author       | varchar(30)  | NO   |     | NULL    |                |
| publication  | varchar(50)  | YES  |     | NULL    |                |
| price        | decimal(5,2) | YES  |     | NULL    |                |
| 出版日期     | date         | YES  |     | NULL    |                |
| comment      | text         | YES  |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
create table `出版社` (
id int primary key auto_increment,
名称 varchar(64),
创刊日期 date,
地址 text,
电话 char(16)
);

create table `作家`(
id int primary key auto_increment,
姓名 varchar(32),
性别 char,
出生日期 date,
住址 text,
风格 text
);

create table `图书`(
id int primary key auto_increment,
书名 varchar(30),
出版日期 date,
定价 decimal(5,2),
a_id int,
p_id int,
constraint a_fk foreign key(a_id) references 作家(id),
constraint p_fk foreign key(p_id) references 出版社(id)
);

-- 出版社--作家关系
create table publication_author(
author_id int not null,
publication_id int not null,
签约时间 datetime default now(),
primary  key(author_id,publication_id),
constraint a_fk2 foreign key(author_id) references 作家(id),
constraint p_fk2 foreign key(publication_id) references 出版社(id)
);

delimiter ##
create function st6(uid1 int,uid2 int)
returns float
begin
set @val1=(select score from cls where id=uid1);
set @val2=(select score from cls where id=uid2);
set @r=@val1-@val2;
return @r;
end ##
delimiter ;


delimiter ##
create procedure get_age(in uid int,out num int)
begin
declare val int;
select age from cls where id=uid into val;
set num=val;
end ##
delimiter ;


create database school;
use school;

create table student(
    s_id varchar(10),
    s_name varchar(20),
    s_age date,
    s_sex varchar(10)
);

create table course(
    c_id varchar(10),
    c_name varchar(20),
    t_id varchar(10)
);


create table teacher (
t_id varchar(10),
t_name varchar(20)
);

create table score (
    s_id varchar(10),
    c_id varchar(10),
    score varchar(10)
);

insert into student (s_id, s_name, s_age, s_sex)
values  ('01' , '赵雷' , '1990-01-01' , '男'),
        ('02' , '钱电' , '1990-12-21' , '男'),
        ('03' , '孙风' , '1990-05-20' , '男'),
        ('04' , '李云' , '1990-08-06' , '男'),
        ('05' , '周梅' , '1991-12-01' , '女'),
        ('06' , '吴兰' , '1992-03-01' , '女'),
        ('07' , '郑竹' , '1989-07-01' , '女'),
        ('08' , '王菊' , '1990-01-20' , '女');

insert into course (c_id, c_name, t_id)
values  ('01' , '语文' , '02'),+
        ('02' , '数学' , '01'),
        ('03' , '英语' , '03');

insert into teacher (t_id, t_name)
values  ('01' , '张三'),
        ('02' , '李四'),
        ('03' , '王五');

insert into score (s_id, c_id, score)
values  ('01' , '01' , 80),
        ('01' , '02' , 90),
        ('01' , '03' , 99),
        ('02' , '01' , 70),
        ('02' , '02' , 60),
        ('02' , '03' , 80),
        ('03' , '01' , 80),
        ('03' , '02' , 80),
        ('03' , '03' , 80),
        ('04' , '01' , 50),
        ('04' , '02' , 30),
        ('04' , '03' , 20),
        ('05' , '01' , 76),
        ('05' , '02' , 87),
        ('06' , '01' , 31),
        ('06' , '03' , 34),
        ('07' , '02' , 89),
        ('07' , '03' , 98);

create table total(
select a.s_id as s_id,a.s_name as s_name,a.s_age as s_age,a.s_sex as s_sex,
b.c_id as c_id,b.score as score,c.t_id as t_id,d.t_name as t_name
from student a
left join
score  b on a.s_id=b.s_id
left join
course c on b.c_id=c.c_id
left join
teacher d on c.t_id=d.t_id
);
select * from total;

查询"01"课程比"02"课程成绩高的学生的信息及课程分数
select * from
(select s_id,score from score where c_id = '01') as a
inner join
(select s_id,score from score where c_id = '02') as b on a.s_id = b.s_id where a.score > b.score;