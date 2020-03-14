use student;
select * from cls;
select * from cls where name like 'J%';
select * from cls where name like '____';
--正则表达式查询
select * from cls where name regexp 'T.+';
select * from cls where name regexp '.+y$';
--as
select name as '姓名',age as '年龄' from cls;
select name as '姓名',age as '年龄' from cls as c where c.score > 90;
--order by,默认为升序排序
select * from cls order by score;
select * from cls order by score desc;
select * from cls where sex = 'w' order by score desc;
select * from cls where sex = 'w' order by age, score desc;

--limit
select * from cls where sex = 'm' limit 1;
select * from cls where sex = 'm' order by score desc limit 1;

--union [all]
select * from cls where sex = 'w';
select * from cls where score < 80;
select * from cls where sex = 'w' union select * from cls where score < 80;
select * from cls where sex = 'w' union all select * from cls where score < 80;

select name from (select name from cls as c where c.age > 15) as s;
select * from cls where name = (select name from cls as c where c.age > 15);