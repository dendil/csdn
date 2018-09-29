#!/usr/local/python3/bin/python3
#-*- coding:utf-8 -*-

import requests
import json
import sys
import os
#企业号及应用相关信息
corp_id='wwe0c2d77a28f790c7'
corp_secret='GNx-afsJ29QQQhJL_-i1npOMm4O7CoHsgN0va0AXzW4'
agent_id='1000004'
#存放access_token文件路径
file_path='/tmp/access_token.log'
file_path_windows='C:/Windows/Temp/access_token.log'
import platform

def TestPlatform():
    print ("----------Operation System--------------------------")
    #Windows will be : (32bit, WindowsPE)
    #Linux will be : (32bit, ELF)
    print(platform.architecture())

    #Windows will be : Windows-XP-5.1.2600-SP3 or Windows-post2008Server-6.1.7600
    #Linux will be : Linux-2.6.18-128.el5-i686-with-redhat-5.3-Final
    print(platform.platform())

    #Windows will be : Windows
    #Linux will be : Linux
    print(platform.system())

    print ("--------------Python Version-------------------------")
    #Windows and Linux will be : 3.1.1 or 3.1.3
    print(platform.python_version())

sysstr = platform.system()
if(sysstr =="Windows"):
    file_path=file_path_windows

if not os.path.exists(file_path):
#    os.mkdir(os.path.split(file_path)[0])
    fp=open(file_path, 'a+')
    fp.close()

def get_access_token_from_file():
  try:
    f=open(file_path,'r+')
    this_access_token=f.read()
#    print('get success %s'%this_access_token)
    f.close()
    return this_access_token
  except Exception as e:
    print(e)
#获取token函数，文本里记录的token失效时调用
def get_access_token():
  get_token_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=%s&corpsecret=%s'%(corp_id,corp_secret)
#  print(get_token_url)
  r=requests.get(get_token_url)
  request_json=r.json()
  this_access_token=request_json['access_token']
#  print(this_access_token)
  r.close()
#把获取到的access_token写入文本
  try:
    f=open(file_path,'w+')
    f.write(this_access_token)
    f.close()
  except Exception as e:
    return this_access_token
#    print(e)
#返回获取到的access_token值

#snedMessage
#死循环，直到消息成功发送
flag=True
while(flag):
#从文本获取access_token
    access_token=get_access_token_from_file()
    if access_token=='':
      access_token = get_access_token()
    try:
     to_user='@all'
     message=sys.argv[3]
#     message='sssssssssssssssssssssssss,,,,,,test,,,,,test'
     send_message_url='https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s'%access_token
#     print(send_message_url)
     message_params={
"touser":to_user,
"msgtype":"text",
"agentid":agent_id,
"text":{"content":message},
"safe":0
}
     r=requests.post(send_message_url,data=json.dumps(message_params))
#     print('post success %s '%r.text)
#判断是否发送成功，如不成功则跑出异常，让其执行异常处理里的函数
     request_json=r.json()
     errmsg=request_json['errmsg']
     if errmsg != 'ok':
       raise
#消息成功发送，停止死循环
     flag=False
    except Exception as e:
      print(e)
      access_token = get_access_token()
