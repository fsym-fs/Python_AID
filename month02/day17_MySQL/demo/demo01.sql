--MySQL存储引擎
--    定义:
--        mysql数据库管理系统中用来处理表的处理器

--1、查看所有存储引擎
   show engines;
--2、查看已有表的存储引擎
   show create table 表名;
--3、创建表指定
   create table 表名(...)engine=MyISAM,charset=utf8,auto_increment=10000;
--4、已有表指定
   alter table 表名 engine=InnoDB;

--explain
explain select * from class_1 where id <5;

--表复制
create table 表名 select 查询命令;

--库备份
--备份
mysqldump -u 用户名 -p 源库名 > ~/stu.sql
--恢复
mysql -u 用户名 -p 目标库名 < stu.sql

--远程登录
mysql -h 192.168.1.6  -u hhh -p