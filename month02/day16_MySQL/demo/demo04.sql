--函数和存储过程

--函数操作
--注意: 1. 函数内的select语句要么return 要么 赋值给变量
--     2. 函数最终return 一个值 而不是一堆值
--     3. 函数里如果有写操作语句则每次调用都会执行，所以慎用
--     4. 一个数据库中函数不能重名
delimiter //
create function st1() returns int
begin
return (select score from cls order by score desc limit 1);
end //
delimiter ;

select st1();

delimiter ##
create function st2(uid int) returns varchar(30)
begin
return (select name from cls where id = uid);
end ##
delimiter ;

delimiter ##
create function st3() returns int
begin
declare a int;
declare b int;
set a = (select score from cls where name = 'Lucy');
select score from cls where name = 'Lily' into b;
return a-b;
end ##
delimiter ;

--存储过程
delimiter ##
create procedure st1()
begin
select name,age from cls;
update cls set sex = 'o' where sex is null;
select name,sex ,score from cls order by score desc;
end ##
delimiter ;
call st1();

--in out inout
delimiter ##
create procedure p_out ( OUT num int )
begin
    select num;
    set num=100;
    select num;
end ##

delimiter ;

set @num=10;
call p_out(@num)

show procedure status like 'st1';
show function status like 'st1';

show create procedure st1;
show create function st1;

--查看所有函数或者存储过程
select name from mysql.proc where db='student' and type='function';
select name from mysql.proc where db='student' and type='procedure';

drop procedure if exists st1;
drop function if exists st1;