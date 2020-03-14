--    `id` int primary key auto_increment,
--    `name` varchar(30) not null,
--    `age` tinyint unsigned,
--    sex enum('m','w','o'),
--    score float default 0.0
--
--create table `interest`
--(
--    id int primary key auto_increment,
--    name varchar(30) not null,
--    hobby set('sing','dance','draw'),
--    level char(2),
--    price decimal(7,2),
--    remark text
--);

use student;
insert into class_1 values (1,'Lily',12,'w', 91.5);
insert into class_1 values (2,'Lucy',14,'w', 90.5);
insert into class_1 values (3,'Tome',16,'m', 81);
insert into class_1 values (4,'Jack',19,'m', 90);
insert into class_1(name,age,sex,score) values ('Jerry',18,'m', 88);

insert into interest values (1,'Emma','sing,dance','B+',1680,'骨骼惊奇');

--          book数据表中插入一些数据
--
--          作者： 老舍   鲁迅  钱钟书  沈从文
--          书的价格  30 -- 120
--          出版社 ：  中国文学  机械工业  中国教育
--create table book
--(
--    id int primary key auto_increment,
--    title varchar(30) not null,
--    author varchar(30) not null,
--    publication varchar(50),
--    price float,
--    comment text
--);
insert into book(title,author,publication,price,comment) values('朝花夕拾','鲁迅','中国文学',39,'好');
insert into book(title,author,publication,price,comment) values('从百草园到三味书屋','鲁迅','中国文学',29,'');
insert into book(title,author,publication,price,comment) values('四世同堂','老舍','中国文学',39,'好');
insert into book(title,author,publication,price,comment) values('藤野先生','鲁迅','中国教育',35,'好');
insert into book(title,author,publication,price,comment) values('围城','钱钟书','机械工业',69,'好');
insert into book(title,author,publication,price,comment) values('边城','沈从文','中国文学',55,'好');