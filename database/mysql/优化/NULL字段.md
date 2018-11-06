# NULL字段
- 建议:以后在建表时额外增加几个无用(备用)的字段 

		create table student(
    	id int not null auto_increment primary key,
    	name char(20),
    	grade_id int,
    	constraint fk_student_grade foreign key(grade_id) references grade(id)
		) engine=innodb default charset=utf8;
		alter 增加一个money 字段

---
		create table student(
    	id int not null auto_increment primary key,
    	name char(20),
    	grade_id int,
    	constraint fk_student_grade foreign key(grade_id) references grade(id),
    	a int null, 
    	b int null,
    	c int null,
    	d int null
		) engine=innodb default charset=utf8; 
		修改备用字段的名或类型，保证以前的数据该字段都有值





