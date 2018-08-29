# 唯一值(unique)
- 优点:
	1. 加速查询
	2. 唯一约束(可以为null)
- 基本写法
	
		create table student(
			nid int,
			sid int,
			name char(20),
			unique uq_nid(nid),
			unique uq_sid(sid)
		) engine=innodb default charset=utf8;

		create table student(
			nid int unique,
			sid int unique,
			name char(20)
		) engine=innodb default charset=utf8;
- 注意:
 
		create table student(
			nid int,
			sid int,
			name char(20),
			unique uq_sp(nid,sid)
		) engine=innodb default charset=utf8;

	- 多条数据,只要sid和nid有一个不同即可
