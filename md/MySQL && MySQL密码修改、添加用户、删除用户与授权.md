# 密码管理

---
## 修改已知原密码
---
- 方法1： 用SET PASSWORD命令 
首先登录MySQL。 
```sql
 set password for root@localhost = password('123'); `
```
- 方法2：用mysqladmin 
```sql
mysqladmin -uroot -p123456 password 123
```
- 方法3：用UPDATE直接编辑user表 
首先登录MySQL。 
```sql
update mysql.user set password=password('123') where user='root' and host='localhost'; 
flush privileges; 
```
## 忘记密码

---
- 修改配置文件
>Default options are read from the following files in the given order:
/etc/mysql/my.cnf /etc/my.cnf ~/.my.cnf 

如果以上配置文件有冲突，那么以最后读取到的为主
`[mysqld] ` 标签添加参数`skip-grant-tables ` 跳过授权表。

	vim /etc/my.cnf
	[mysqld]
	skip-grant-tables  跳过授权表
	datadir=/var/lib/mysql
	socket=/var/lib/mysql/mysql.sock
	user=mysql
	Disabling symbolic-links is recommended to prevent assorted security risks
	symbolic-links=0

	[mysqld_safe]
	log-error=/var/log/mysqld.log
	pid-file=/var/run/mysqld/mysqld.pid
然后执行修改已知密码的 **方法1** 或 **方法3** 操作
- 直接以后台安全进程启动mysql
```bash
/usr/bin/mysqld_safe --skip-grant-tables &
```
然后执行已知密码的 **方法1** 或 **方法3** 操作

# 用户管理
---
## 1、创建用户
```sql
create user user@host;
create user user@host identified by 'password';
```
@`localhost` 表示用户只能在本地登录
@`%`			表示在任何一台电脑上都可以登录
@`ip`			表示在指定IP电脑上可以登录
@`domain`	表示在指定域名下可以登录

or
```sql
insert into mysql.user(Host,User,Password) values("localhost","test",password("1234"));
```

用户的信息保存在mysql数据库中的user表中，验证用户是否创建成功如下：
```sql
select user,host,password from mysql.user;	    
```
## 2、用户权限
- 权限分类：

|  |  |
|--|--|
| USAGE | 无权限,只有登录数据库,只可以使用test或test_*数据库 |
|ALL   | 所有权限 |
|select/update/delete/super/slave/reload|指定的权限|
|with grant option|允许把自己的权限授予其它用户或者从其他用户收回自己的权限|


- 作用范围：

|  |  |
|--|--|
| \*.*	|		            全库、全表（mysql.user）|
mysql.*		        | mysql库下所有表（某库中的所有表）(mysql.db)|
mysql.user		     | mysql库中user表（单表）(mysql.table_priv)|
mysql.user.host     |mysql库中user表的host列(mysql.columns_priv)|

- 主机登录权限：

|  |  |
|--|--|
user@localhost		     |                       表示user只能在本地通过socket登录服务器
user@192.168.0.1	            |                表示user用户只能在192.168.0.1登录数据库服务器
user@192.168.0.0/255.555.255.0    |   指定某个子网的主机可以登录数据库
user@%				                          |  表示user用户能在所有的机器上登录数据库服务器

- 用户授权：

 授权test用户拥有testDB数据库的所有权限（某个数据库的所有权限）
 格式：grant 权限 on 数据库.* to 用户名@登录主机 identified by "密码";
 ```sql
grant all privileges on testDB.* to test@localhost identified by '1234';
flush privileges;//刷新系统权限表
```
如果想指定部分权限给一用户，可以这样来写:
```sql
grant select,update on testDB.* to test@localhost identified by '1234';
flush privileges; //刷新系统权限表
```
授权test用户拥有所有数据库的某些权限： 　 
```sql
grant select,delete,update,create,drop on *.* to test@"%" identified by "1234";
```
test用户对所有数据库都有`select,delete,update,create,drop` 权限。
`@"%"` 表示对所有非本地主机授权，不包括`localhost`。（localhost地址设为127.0.0.1，如果设为真实的本地地址，不知道是否可以，没有验证。）

对localhost授权：
```sql
grant all privileges on testDB.* to test@localhost identified by '1234';
```

- 权限的保存位置：

|  |  |
|--|--|
mysql.user		|	所有mysql用户的账号和密码，以及对用户对全库全表权限（*.*）
mysql.db			|	非mysql库的授权都保存在此(db.*)
mysql.table_priv|		某库某表的授权(db.table)
mysql.columns_priv|		某库某表某列的授权(db.table.col1)
mysql.procs_priv|		某库存储过程的授权

- 回收权限：revoke

```sql
revoke update,select on mysql.user from test@localhost;  	撤消指定的权限
revoke all privileges,grant option from test@'%';           撤消所有的权限
```
- 删除用户：
```sql
drop user user01@'localhost';	                            删除用户
```
```sql
select user from mysql.user where user='user01';	       验证用户是否删除成功
```
```sql
drop user user;                                          默认删除该用户从任意主机登陆
```
```sql
rename user test01@'instructor.example.com' to test001@'localhost';  重命名用户名
```
```sql
show grants;                                              查看用户权限
```
```sql
show grants for user02@'%';                               查看指定用户的权限 
```
```sql
drop user ''@'rhel6.example.com';                        删除一个匿名用户
```
```sql
delete from mysql.user where user='';		            删除mysql中的匿名用户
```
```sql
delete from mysql.user where user='root' and host='::1';     删除mysql中ipv6
```
```sql
flush privileges;
```

