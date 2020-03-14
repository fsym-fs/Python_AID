select country,avg(attack) from sanguo group by country;
select country,avg(attack) from sanguo group by country having avg(attack) > 260;
select distinct country from sanguo;
select count(distinct country) from sanguo;