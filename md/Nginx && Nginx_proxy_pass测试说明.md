第一种：

location /proxy/ {
     proxy_pass http://127.0.0.1:81/;
}

会被代理到http://127.0.0.1:81/test.html 这个url
 
第二咱(相对于第一种，最后少一个 /)

location /proxy/ {
     proxy_pass http://127.0.0.1:81;
}

会被代理到http://127.0.0.1:81/proxy/test.html 这个url
 
第三种：

location /proxy/ {
     proxy_pass http://127.0.0.1:81/ftlynx/;
}

会被代理到http://127.0.0.1:81/ftlynx/test.html 这个url。
 
第四种情况(相对于第三种，最后少一个 / )：

location /proxy {
     proxy_pass http://127.0.0.1:81/ftlynx;
}

会被代理到http://127.0.0.1:81/ftlynxtest.html 这个url
