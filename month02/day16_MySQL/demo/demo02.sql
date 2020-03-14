select * from dept,person where dept.id = person.dept_id;

--内连接
select * from person inner join  dept  on  person.dept_id =dept.id where age > 20;

--笛卡尔积
select * from person inner join  dept;

--外连接
--左连接 : 左表为主表，显示右表中与左表匹配的项
select * from person left join  dept  on  person.dept_id =dept.id;
--右连接 : 右表为主表，显示左表中与右表匹配的项
select * from person right join  dept  on  person.dept_id =dept.id;
--注意：我们尽量使用数据量大的表作为基准表，即左连接做左表，右连接做右表