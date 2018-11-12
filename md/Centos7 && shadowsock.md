# 服务端
## 1、安装python-pip 及epel仓库
```
yum install -y python-pip epel-release vim
```
## 2、安装shadowsocks
```
pip install shadowsocks
```
## 3、配置shadowsocks
```
cat >> /etc/shadowsocks.json<<EOF
{
    "server":"0.0.0.0",
    "server_port":8080,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword123",
    "timeout":300,
    "method":"aes-256-cfb"
}
EOF
```
## 4、启动shadowsocks
```
ssserver -c /etc/shadowsocks.json -d start
```
### 5、关闭shadowsocks
```
ssserver -c /etc/shadowsocks.json -d stop
```
### 6、加入开机启动
```
echo 'ssserver -c /etc/shadowsocks.json -d start'>> /etc/rc.local
```
```
chmod +x /etc/rc.local
```


# Firewalld 防火墙配置
打开 /etc/firewalld/zones/public.xml 文件，使用 `<port protocol=”网路协议” port=”指定端口”/>` 开放相应的端口：
`<?xml version="1.0" encoding="utf-8"?>
<zone>
<short>Public</short>
<description>For use in public areas. You do not trust the other computers on networks to not harm your computer. Only selected incoming connections are accepted.</description>
<service name="dhcpv6-client"/>
<port protocol="tcp" port="指定端口"/>
<port protocol="tcp" port="开始端口-结束端口"/>
<port protocol="udp" port="开始端口-结束端口"/>
</zone>`
重启 Firewalld 并查看端口配置是否生效
```
service firewalld restart
systemctl enable firewalld
firewall-cmd --zone=public --list-all
```
