# 外键(foreign key)
- 基本代码
		
		create table grade(
			id int not null auto_increment primary key,
			title char(20)
		) engine=innodb default charset=utf8;
		
		create table student(
			id int not null auto_increment primary key,
			name char(20),
			grade_id int,
			constraint fk_student_grade foreign key (grade_id)
			references grade (id)
		) engine=innodb default charset=utf8;

		insert into grade values(0,'python01'),(0,'python02'),(0,'python03');
		insert into student values(0, 'tom1', 1)

- 主表从表: 声明关系的表示从表

- 一对多: 外键在多的一方
	- 学生表与班级表
		- 学生:
				
				1	tom1	1
				2	tom2	1
				3	tom3	2
				4	tom4	3
		- 班级表
					
				1	python01
				2	python02
				3	python03

- 一对一:
	- 用户表与仓库表
		- 用户表

				1	zahir
				2	tom	
				3	sunck		
				4	sony

		- 仓库表
			
				1	zahir/	1
				2	tom/	2	
	- 应用:表的字段太多,需要拆分

- 多对多:
	- 原理: 底层是通过两个外键实现,两个外键存在一张关系表中

	- user表
	- host表
	- user2host表 