insert into dept values
(1,'技术部'),
(2,'财务部'),
(3,'销售部'),
(4,'行政部'),
(5,'市场部');
insert into person values
(1,'小聪',19,'男',5000,2020-6-5,1),
(2,'小航',20,'男',5000,2020-6-3,4),
(3,'小翔',19,'男',5000,2020-6-5,3),
(4,'小博',21,'男',4600,2020-6-9,4),
(5,'小才',23,'男',4800,2020-6-2,2),
(6,'小艾',23,'男',4800,2020-6-9,5);
insert into person values
(7,'Lily',29,'w',20000,'2017-4-3',2),
(8,'Tom',27,'m',16000,'2019-10-3',1),
(9,'Joy',32,'m',34000,'2016-5-20',1),
(10,'Emma',29,'w',12000,'2018-7-7',4),
(11,'Baron',24,'m',15000,'2019-3-29',5),
(12,'Abby',30,'w',18000,'2018-11-3',3);
alter table person add constraint dept_fk foreign key(dept_id) references dept(id);
desc person;
show create table person;]

alter table person drop foreign key dept_fk;
drop index dept_fk on person;

alter table person drop foreign key dept_fk;

--级联动作
alter table person add constraint dept_fk foreign key(dept_id) references dept(id) on delete cascade on update cascade;

alter table person drop foreign key dept_fk;
alter table person add constraint dept_fk foreign key(dept_id) references dept(id) on delete set null on update set null;
