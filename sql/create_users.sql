create database teste;
use teste;
create table users (
	id int not null auto_increment primary key,
	name varchar(100) not null,
    email varchar(100) not null,
    created datetime not null
    );
    desc users