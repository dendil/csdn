### 1. 如何让nginx显示文件夹目录

```bash
vim /etc/nginx/conf.d/default.conf
```
添加如下内容：

	location / {   
        root /data/www/file                     //指定实际目录绝对路径；   
        autoindex on;                            //开启目录浏览功能；   
        autoindex_exact_size off;            //关闭详细文件大小统计，让文件大小显示MB，GB单位，默认为b；   
        autoindex_localtime on;              //开启以服务器本地时区显示文件修改日期！   
	}



### 2. 只打开网站部分目录浏览功能

只打开http://www.******.com/soft 目录浏览

```bash
vim  /usr/local/nginx/conf/nginx.conf   #编辑配置文件，在server {下面添加以下内容：
```
	location   /soft {
	autoindex on;
	autoindex_exact_size off;
	autoindex_localtime on;
     }
                      
