 
1: 安装必要的一些系统工具
```sh
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```
2: 添加软件源信息
```sh
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```
or国外节点
```bash
sudo yum-config-manager     --add-repo     https://download.docker.com/linux/centos/docker-ce.repo
```
Step 3: 更新并安装 Docker-CE
```sh
sudo yum makecache fast
sudo yum -y install docker-ce
```
4: 开启Docker服务
```sh
systemctl start docker.service 
```
