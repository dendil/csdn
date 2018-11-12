
安装MariaDB
### 2.3.1 [通过yum安装MariaDB][1]
本人使用的版本为 10.3.9 [点击此处选择其他版本][2]
-   清除现有依赖
```bash
rpm -qa | grep mariadb |xargs rpm -e --nodeps
rpm -qa | grep mysql |xargs rpm -e --nodeps
```
- 添加yum源 repo
```bash
vim 	/etc/yum.repos.d/MariaDB-10.3.repo
```
		# MariaDB 10.3 CentOS repository list - created 2018-08-21 05:52 UTC
		# http://downloads.mariadb.org/mariadb/repositories/
		[mariadb]
		name = MariaDB
		baseurl = http://yum.mariadb.org/10.3/centos7-amd64
		gpgkey=https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
		gpgcheck=1
or
```bash
wget -O /etc/yum.repo.d/MariaDB-10.3.repo https://raw.githubusercontent.com/dendil/csdn/master/yum.repo.d/MariaDB-10.3.repo
```
- 导入GPG key
```bash
rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB
```
- 安装MariaDB
```bash
yum install -y MariaDB-server MariaDB-client
```
- 启动MariaDB
```bash
systemctl start mariadb
```
- 登录到数据库
	用`mysql -uroot`命令登录到MariaDB，首次登陆时`root`账户的密码为空。

- MariaDB 初始化
```bash
mysql_secure_installation
```
		Enter current password for root (enter for none):<–初次运行直接回--设置密码
		Set root password? [Y/n] <– 是否设置root用户密码，输入y并回车或直接回车
		New password: <– 设置root用户的密码
		Re-enter new password: <– 再输入一次你设置的密码
		Remove anonymous users? [Y/n] <– 是否删除匿名用户，回车
		Disallow root login remotely? [Y/n] <–是否禁止root远程登录,回车,
		Remove test database and access to it? [Y/n] <– 是否删除test数据库，回车
		Reload privilege tables now? [Y/n] <– 是否重新加载权限表，回车
初始化MariaDB完成，接下来测试登录

```bash
mysql -uroot -ppassword
```
 











[1]: https://mariadb.com/kb/en/library/yum/
[2]: https://downloads.mariadb.org/mariadb/repositories/#mirror=tuna
