# CDN的配置回源host与源站的区别



---

 

#### 源站：  源站决定了回源时，请求到哪个IP

#### 回源host：回源host决定回源请求访问到该IP上的哪个站点

 

 

 
----

### 例子1：源站是域名
源站为www.a.com 回源host为www.b.com

那么实际回源是请求到www.a.com解析到的IP，对应的主机上的站点www.b.com

 

 

### 例子2：源站是IP

源站为1.1.1.1 回源host为www.b.com

那么实际回源的是1.1.1.1对应的主机上的 站点www.b.com

