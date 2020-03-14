system clear
show databases;
use database;
select database();
drop database student;
show databases;
desc 表名;
drop table 表名;

create table `class_1`
(
    `id` int primary key auto_increment,
    `name` varchar(30) not null,
    `age` tinyint unsigned,
    sex enum('m','w','o'),
    score float default 0.0
);


create table `interest`
(
    id int primary key auto_increment,
    name varchar(30) not null,
    hobby set('sing','dance','draw'),
    level char(2),
    price decimal(7,2),
    remark text
);