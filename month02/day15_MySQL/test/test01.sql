使用book表完成
id           | int(11)      | NO   | PRI | NULL    | auto_increment |
| title        | varchar(30)  | NO   |     | NULL    |                |
| author       | varchar(30)  | NO   |     | NULL    |                |
| publication  | varchar(50)  | YES  |     | NULL    |                |
| price        | decimal(5,2) | YES  |     | NULL    |                |
| 出版日期     | date         | YES  |     | NULL    |                |
| comment
1.统计每位作家写的图书的平均价格
select author,avg(price) from book group by author;
2.统计每个出版社出版图书的数量
select publication,count(*) from book group by publication;
3.查看总共有多少个出版社
select count(distinct publication) from book;
4.筛选出那些出版过40元图书的出版社，并按照价格倒序排序
select publication,max(price)
from book group by publication
having max(price)>40
order by max(price) desc;
5.统计所有出版时间的图书的平均价格
select title,avg(price),出版日期 from book group by 出版日期;