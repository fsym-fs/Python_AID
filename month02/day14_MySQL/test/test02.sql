--test
--使用book表完成
--1.将呐喊的价格改为45元
--2.增加一个字段，出版日期，类型为date 放在价格后面
--3.修改所有老舍的作品的池出版日期为2016-10-1
--4.修改所以人民文学出版社的图书作品出版日期为2018-1-1，但是老舍的不改
--5.删除所有在60元以上的图书
--6.修改价格字段的数据类型为decimal(5,2)
--7.查找鲁迅写的早2017年以后出版的图书
update book set price = 45 where title = '呐喊';
alter table book add 出版日期 date after price;
update book set 出版日期 = "2016-10-1" where author = '老舍';
update book set 出版日期 = "2018-1-1" where publication='中国文学出版社' and author != '老舍';
delete from book where price>60;
alter table book modify price decimal(5,2);
select * from book where author = '鲁迅' and 出版日期 >='2017-01-01';