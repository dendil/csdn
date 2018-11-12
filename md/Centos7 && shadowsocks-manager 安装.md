# 安装
---
## 1.安装 shadowsocks-libev
---
```bash
sudo  yum-config-manager --add-repo https://copr.fedorainfracloud.org/coprs/librehat/shadowsocks/repo/epel-7/librehat-shadowsocks-epel-7.repo
```
```bash
yum install shadowsocks-libev -y
```
## 2.安装 Node.js 8.*
---
```bash
curl --silent --location https://rpm.nodesource.com/setup_8.x | sudo bash -
```
```bash
yum install -y nodejs
```
## 3.安装 ssmgr
---
```bash
npm i -g shadowsocks-manager --unsafe-perm
```	
```bash
cd /usr/lib/node_modules/shadowsocks-manager/
```
```bash
npm install sqlite3 --save
```
##   使用
---
1.在每台机上启动shadowsocks，需要指定 manager address，启动后会监听这个 udp 端口：
```bash
ss-manager -m aes-256-cfb -u --manager-address 127.0.0.1:4000
```
2.在每台机的~/.ssmgr路径下新建配置文件ss.yml，内容如下：
```bash
type: s
  shadowsocks:
  address: 127.0.0.1:4000
  #这里的地址和端口需要跟上一步的 --manager-address 参数保持一致，连接上述 udp 端口
manager:
  address: 0.0.0.0:4001
  #这个 address 参数会让程序监听一个 tcp 端口，用于接收 webgui 发送过来的控制命令
  password: '123456'
  db: 'ss.sqlite'
```
3.在每台机的启动ssmgr：
```bash
ssmgr -c ss.yml
```
4.然后是使用 webgui 这个 plugin，这部分可以在3台机的其中一台运行，也可以运行在其他位置，本文假设运行在同一台机上，首先在路径~/.ssmgr下添加配置文件webgui.yml：
```bash
type: m
manager:
  address: 1.1.1.1:4001
  password: '123456'
  # 这部分的端口和密码需要跟上一步 manager 参数里的保持一致，以连接 type s 部分监听的 tcp 端口
plugins:
flowSaver:
    use: true
  user:
    use: true
  account:
    use: true
  macAccount:
    use: true
  group:
    use: true
  email:
    use: true
    type: 'smtp'
    username: 'username'
    password: 'password'
    host: 'smtp.your-email.com'
    # 这部分的邮箱和密码是用于发送注册验证邮件，重置密码邮件
  webgui:
    use: true
    host: '0.0.0.0'
    port: '80'
    site: 'http://yourwebsite.com'
    # cdn: 'http://xxx.com' # 静态资源cdn地址，可省略
    # icon: 'icon.png' # 自定义首页图标，默认路径在 ~/.ssmgr 可省略
    # skin: 'default' # 首页皮肤，可省略
    # googleAnalytics: 'UA-xxxxxxxx-x' # Google Analytics ID，可省略
    gcmSenderId: '456102641793'
    gcmAPIKey: 'AAAAGzzdqrE:XXXXXXXXXXXXXX'
  webgui_telegram: // telegram 机器人的配置，可省略
    use: true
    token: '191374681:AAw6oaVPR4nnY7T4CtW78QX-Xy2Q5WD3wmZ'
  alipay:
    # 如果不使用支付宝，这段可以去掉
    use: true
    appid: 2015012108272442
    notifyUrl: 'http://yourwebsite.com/api/user/alipay/callback'
    merchantPrivateKey: 'xxxxxxxxxxxx'
    alipayPublicKey: 'xxxxxxxxxxx'
    gatewayUrl: 'https://openapi.alipay.com/gateway.do'
  paypal:
    # 如果不使用paypal，这段可以去掉
    use: true
    mode: 'live' # sandbox or live
    client_id: 'At9xcGd1t5L6OrICKNnp2g9'
    client_secret: 'EP40s6pQAZmqp_G_nrU9kKY4XaZph'

db: 'webgui.sqlite'
```


5.然后再启动一个ssmgr，就可以运行webgui了：
```bash
ssmgr -c webgui.yml
```
6.如果上面的配置一切正常的话，打开http://yourwebsite.com就可以看到注册界面了，注册一个帐号，首个注册的帐号即为管理员

---
## 后台运行
```bash
screen -dmS ss-manager ss-manager -m aes-256-cfb -u --manager-address 127.0.0.1:4000
screen -dmS ss ssmgr -c ~/.ssmgr/ss.yml
screen -dmS webgui ssmgr -c ~/.ssmgr/webgui.yml
```
## 配合nginx使用
---
如果80端口还有别的网站占用，或者需要采用 https 的方式访问（强烈推荐），需要先配置nginx服务器：
1.把配置文件的 webgui 部分更改为：
```bash
webgui:
  use: true
  host: '127.0.0.1'
  port: '8080'
  site: 'http://yourwebsite.com'

添加 nginx 的配置文件：

server {
  listen         80;
  server_name    yourwebsite.com;
  rewrite ^(.*) https://$host$1 permanent;
}
server {  
  listen                 443 ssl http2;
  server_name            yourwebsite.com;
  ssl                    on;
  ssl_certificate        /xxx/chained.pem;
  ssl_certificate_key    /xxx/domain.key;
  location / {
  proxy_set_header   X-Real-IP $remote_addr;
  proxy_set_header   Host      $http_host;
  proxy_pass         http://127.0.0.1:8080;
  }
}
```
---
