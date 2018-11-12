##更换内核
```bash
curl https://www.zhangfangzhou.cn/sh/ruisu.sh |sh
```
##安装91yun锐速
```bash
wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh
```
##卸载锐速
```bash
chattr -i /serverspeeder/etc/apx* && /serverspeeder/bin/serverSpeeder.sh uninstall -f
```
## 启动停止状态

```bash
/serverspeeder/bin/serverSpeeder.sh  {status|start|stop}
```
