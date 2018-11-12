
# 目录
@[toc]
##1. 前言
java对接C,引用到了 jna，报出如下错误

java.lang.UnsatisfiedLinkError: The specified module could not be found.
```java
Exception in thread "main" java.lang.UnsatisfiedLinkError: The specified module could not be found.
at com.sun.jna.Native.open(Native Method)
at com.sun.jna.Native.open(Native.java:1759)
at com.sun.jna.NativeLibrary.loadLibrary(NativeLibrary.java:260)
at com.sun.jna.NativeLibrary.getInstance(NativeLibrary.java:398)
at com.sun.jna.Library$Handler.<init>(Library.java:147)
at com.sun.jna.Native.loadLibrary(Native.java:412)
at com.sun.jna.Native.loadLibrary(Native.java:391)
```
```java
Exception in thread "main" java.lang.UnsatisfiedLinkError: 找不到指定模块.
at com.sun.jna.Native.open(Native Method)
at com.sun.jna.Native.open(Native.java:1759)
at com.sun.jna.NativeLibrary.loadLibrary(NativeLibrary.java:260)
at com.sun.jna.NativeLibrary.getInstance(NativeLibrary.java:398)
at com.sun.jna.Library$Handler.<init>(Library.java:147)
at com.sun.jna.Native.loadLibrary(Native.java:412)
at com.sun.jna.Native.loadLibrary(Native.java:391)
```
## 2. 思路
各种百度 google 所有方法都试了，错误还是没法解决。
项目源码 如下图 dll 动态执行库
java.lang.UnsatisfiedLinkError出现这种错误的原因是一般是java虚拟机找不到声明为native方法的本地语言定义时，出现的错误。在我的理解过程中我一般都认为是由于导入dll或者导入lib文件不正确导致的.
遂思路转向 gtp.dll  的依赖 参考[github  tess4j  issues][14]发现神器       [Dependency Walker][15]
![csdn_20180813154138.png][1]



## 3. 神器 Dependency Walker

Dependency Walker [官方网站][13]http://www.dependencywalker.com/
Dependency Walker 是 Microsoft Visual C++ 中提供的非常有用的 PE 模块依赖性分析工具。主要功能如下： 
	查看 PE 模块的导入模块。 
	查看 PE 模块的导入和导出函数。 
	动态剖析 PE 模块的模块依赖性。 
	解析 C++ 函数名称。
Dependency Walker [使用说明][12]  http://www.dependencywalker.com/help/html/contents.htm
![csdn_20180813161354.png][2]


下载好了之后  
![csdn_20180813171404.png][3]


-------------------
打开 depends.exe

左上角  file --》 open   --》 选择 调用的 dll 文件
![csdn_20180813161916.png][4]



果不其然发现动态库组件 缺失   黄色叹号
![csdn_20180813162549.png][5]


## 4. 下载 dll文件 
![csdn_20180813162955.png][6]


### 4.1 下载UCRTBASED.DLL
参考[如何解决vs2015运行缺少ucrtbased.dll的问题][16]下载UCRTBASED.DLL
https://jingyan.baidu.com/article/1e5468f96a8048484861b711.html
#### 4.1.1 搜索UCRTBASED.DLL
![csdn_20180813163557.png][7]

#### 4.1.2 下载保存UCRTBASED.DLL
![csdn_20180813164404.png][8]
![csdn_20180813164847.png][9]

#### 4.1.3 解压到指定目录
![csdn_20180813171110.png][10]


- 1、**Windows 95/98/Me系统**，将ucrtbased.dll复制到C:\Windows\System目录下。
- 2、**Windows NT/2000系统**，将ucrtbased.dll复制到C:\WINNT\System32目录下。
- 3、**Windows XP/WIN7/win10系统**
如果您的系统是   **64位**   的请将ucrtbased.dll文件复制到C:\Windows\SysWOW64目录下，
如果您的系统是   **32位**   的请将ucrtbased.dll文件复制到C:\Windows\System32目录下。
具体的方法可以参考这篇文章：[win7 64位旗舰版系统运行regsvr32.exe提示版本不兼容][17]

## 安装所有依赖
参考 第四部[下载 dll文件][18]安装所有依赖
![csdn_20180813170749.png][11]




结束

---
[1]: http://img.caojie.top/kspn/images/java/csdn_20180813154138.png
[2]: http://img.caojie.top/kspn/images/java/csdn_20180813161354.png
[3]: http://img.caojie.top/kspn/images/java/csdn_20180813171404.png
[4]: http://img.caojie.top/kspn/images/java/csdn_20180813161916.png
[5]: http://img.caojie.top/kspn/images/java/csdn_20180813162549.png
[6]: http://img.caojie.top/kspn/images/java/csdn_20180813162955.png
[7]: http://img.caojie.top/kspn/images/java/csdn_20180813163557.png
[8]: http://img.caojie.top/kspn/images/java/csdn_20180813164404.png
[9]: http://img.caojie.top/kspn/images/java/csdn_20180813164847.png
[10]: http://img.caojie.top/kspn/images/java/csdn_20180813171110.png
[11]: http://img.caojie.top/kspn/images/java/csdn_20180813170749.png
[12]: http://www.dependencywalker.com/help/html/contents.htm
[13]: http://www.dependencywalker.com/
[14]: https://github.com/nguyenq/tess4j/issues/95
[15]: http://www.dependencywalker.com/
[16]: https://jingyan.baidu.com/article/1e5468f96a8048484861b711.html
[17]: https://www.jb51.net/os/windows/182610.html
[18]: https://blog.csdn.net/weixin_38111667/article/details/81630290#4-%E4%B8%8B%E8%BD%BD-dll%E6%96%87%E4%BB%B6
