--索引

--普通索引
create table index_test
(
    id int primary key auto_increment,
    name varchar(20),
    index name_index (name)
);

--唯一索引
create table index_test
(
    id int primary key auto_crement,
    name varchar(20),
    unique(name)
);

create unique index name_index on index_test(name);

desc index_test;
show index from index_test;
drop index name_index on index_test;