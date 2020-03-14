create table stu
(
    id int primary key auto_increment,
    姓名 varchar(30),
    年龄 tinyint,
    性别 char,
    籍贯 varchar(128)
);
create table teacher
(
    id int primary key auto_increment,
    姓名 varchar(30),
    职称 varchar(30),
    年龄 tinyint
);
create table course
(
    id int primary key auto_increment,
    名称 varchar(30),
    学分 float,
    tid int,
    constraint t_fk foreign key(tid) references teacher(id)
);
create table course_stu
(
    cid int,
    sid int,
    primary key(cid,sid),
    score float,
    constraint c_fk foreign key(cid) references course(id),
    constraint s_fk foreign key(sid) references stu(id)
);