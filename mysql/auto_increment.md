# auto_increment
- 作用: 自增长
- 注意: 对于自增长列,必须是索引(含主键)

- 原理: 使用show create table 表名 \G 语句可以查看建表语句,第一次查看不到什么特殊情况,插入一条数据后再查看发现后面多了AUTO_INCREMENT=值,下次再插入数据时,表中的主键的值为刚才看到的AUTO_INCREMENT的值,并且AUTO_INCREMENT值按步长为1递增
- alter table 表名 AUTO_INCREMENT=值
- eg. alter table student AUTO_INCREMENT=5;

mysql 基于会话级别
- 
1. 自身会话
	- show session variables like 'auto_inc%';
	- set session auto_increment_increment=2; /*修改步长*/

2. 全局会话
	- show global variables like 'auto_inc%';
	- set global auto_increment_increment=2;
	