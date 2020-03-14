select cls.name, interest.hobby ,interest.price from cls inner join interest on cls.name = interest.name;

select cls.name,cls.sex,i.hobby from cls left join interest as i on cls.name = i.name;

select i.hobby,i.price,c.name from cls as c right join interest as i on c.name = i.name;