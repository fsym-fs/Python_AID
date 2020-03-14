create database relevance charset=utf8;
use relevance;

create table student
(
    id int primary key auto_increment,
    name varchar(50) not null
);
create table record
(
    id int primary key auto_increment,
    comment text not null,
    st_id int unique,
    foreign key(st_id) references student(id)
    on delete cascade
    on update cascade
);

create table person(
  id varchar(32) primary key,
  name varchar(30),
  sex char(1),
  age int
);
create table car(
  id varchar(32) primary key,
  name varchar(30),
  price decimal(10,2),
  pid varchar(32),
  constraint car_fk foreign key(pid) references person(id)
);

create table athlete
(
    id int primary key auto_increment not null,
    name varchar(30) default null,
    age tinyint not null,
    country varchar(30) not null,
    description varchar(30) default null
);
create table item
(
    id int primary key auto_increment not null,
    rname varchar(30) not null
);
create table athlete_item
(
    aid int not null,
    tid int not null,
    primary key(aid,tid),
    constraint athlete_fk foreign key(aid) references athlete(id),
    constraint item_fk foreign key(iid) references item(id)
);
