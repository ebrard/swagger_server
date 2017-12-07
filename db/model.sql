drop table if exists  "Category" ;
drop table if exists Pet ;

create table Category (
	_id INT primary key,
	_name varchar(400)
) ;

create table Pet (
	_id int primary key,
	_category_id int,
	_status varchar(500),
	_name varchar(100),
	FOREIGN KEY(_category_id) REFERENCES Category(_id)
) ;
