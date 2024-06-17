drop database if exists ComedorConecta;
create database ComedorConecta;
use ComedorConecta;

create table users(
id			int				auto_increment primary key,
username	varchar(100)	unique not null collate utf8_bin,
email		varchar(300)	unique not null collate utf8_bin,
passwd		varchar(255)	not null,
centro		varchar(200) 	not null,
telefono 	varchar(15)		null
);

create table cursos(
curso		varchar(5)				primary key not null
);
insert into cursos values ('1');
insert into cursos values ('2');
insert into cursos values ('3');
insert into cursos values ('4');
insert into cursos values ('5');
insert into cursos values ('6');


create table alumno(
numero				int				primary key unique,
primerApellido		varchar(200)	not null collate utf8_bin,
segundoApellido		varchar(200)	not null collate utf8_bin,
curso				char			not null,
ensenanza			varchar(200) 	not null collate utf8_bin,
grupo				varchar(50)		not null,
nombre				varchar(200)	not null collate utf8_bin
);

create table madre(
id			int 			primary key auto_increment,
nombre		varchar(200)	not null collate utf8_bin,
num_hijo 	int				not null,
email		varchar(100) 	not null collate utf8_bin,
direccion	varchar(200)	not null collate utf8_bin,	
constraint fk_num_hijo foreign key (num_hijo) references alumno (numero)
	on delete cascade on update cascade
);