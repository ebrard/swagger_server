drop table if exists  "Category" ;
drop table if exists Pet ;
drop table if exists Tag ;
drop table if exists PetTags ;

create table Category (
	_id INT primary key,
	_name varchar(400)
) ;

create table Pet (
	_id int primary key,
	_category_id int,
	_tag_id int,
	_status varchar(500),
	_name varchar(100),
	FOREIGN KEY(_category_id) REFERENCES Category(_id),
	FOREIGN KEY(_tag_id) REFERENCES Tag(_id)
) ;

create table Tag (
    _id int primary key,
    _name varchar(50)
) ;

create table PetTags (
    pet_id int,
    tag_id int
) ;