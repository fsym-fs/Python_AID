select * from book where price between 30 and 40;
select * from book where publication='中国教育出版社';
select * from book where author='老舍' and publication='中国文学出版社';
select * from book where comment is not null;
select title,price from book where price > 60;
select * from book where author in ('鲁迅','矛盾');