create database books character set utf8;
use books;
create table book
(
    id int primary key auto_increment,
    title varchar(30) not null,
    author varchar(30) not null,
    publication varchar(50),
    price float,
    comment text
);