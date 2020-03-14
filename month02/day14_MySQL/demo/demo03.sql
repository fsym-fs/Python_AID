select max(attack) as 最大攻击力 from sanguo;
select * from sanguo where attack = (select max(attack) as 最大攻击力 from sanguo);
select avg(attack) as 平均攻击力 from sanguo;
select avg(attack) as 平均攻击力,max(attack) as 最大攻击力 from sanguo;
select sum(attack) as 攻击力和 from sanguo;
select count(*) as 总人数 from sanguo;
select count(*) as 总人数 from sanguo where country = '蜀';
select gender, count(*) as 总人数 from sanguo group by gender;
select country, avg(attack) as 平均攻击力,max(attack) as 最大攻击力 from sanguo group by country;
select country,count(id) as number from sanguo
where gender = '男' group by country
order by number desc
limit 2;