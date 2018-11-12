目录

@[toc]
# 什么是Docker
---

![docker_logo.png][27]

>Docker是一个开源的应用容器引擎，诞生于 2013 年初，基于 Go 语言 并遵从Apache2.0协议开源。可以轻松的为任何应用创建一个轻量级的、可移植的、自给自足的容器。
Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以批量地在生产环境中部署，包括VMs（虚拟机）、bare metal、OpenStack 集群和其他的基础应用平台。
Docker容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。
Docker 项目的目标是实现轻量级的操作系统虚拟化解决方案。
Docker 的基础是 Linux 容器（LXC）等技术。在 LXC 的基础上 Docker 进行了进一步的封装，让用户不需要去关心容器的管理，使得操作更为简便。用户操作 Docker 的容器就像操作一个快速轻量级的虚拟机一样简单。







# 为什么用Docker

----

作为一种新兴的虚拟化方式，Docker 跟传统的虚拟化方式相比具有众多的优势。
Docker 在如下几个方面具有较大的优势：

* 更快速的交付和部署
Docker在整个开发周期都可以完美的辅助你实现快速交付。Docker允许开发者在装有应用和服务本地容器做开发。可以直接集成到可持续开发流程中。
例如：开发者可以使用一个标准的镜像来构建一套开发容器，开发完成之后，运维人员可以直接使用这个容器来部署代码。 Docker 可以快速创建容器，快速迭代应用程序，并让整个过程全程可见，使团队中的其他成员更容易理解应用程序是如何创建和工作的。 Docker 容器很轻很快！容器的启动时间是秒级的，大量地节约开发、测试、部署的时间。
* 高效的部署和扩容
Docker 容器几乎可以在任意的平台上运行，包括物理机、虚拟机、公有云、私有云、个人电脑、服务器等。 这种兼容性可以让用户把一个应用程序从一个平台直接迁移到另外一个。
Docker的兼容性和轻量特性可以很轻松的实现负载的动态管理。你可以快速扩容或方便的下线的你的应用和服务，这种速度趋近实时。
* 更高的资源利用率
Docker 对系统资源的利用率很高，一台主机上可以同时运行数千个 Docker 容器。容器除了运行其中应用外，基本不消耗额外的系统资源，使得应用的性能很高，同时系统的开销尽量小。传统虚拟机方式运行 10 个不同的应用就要起 10 个虚拟机，而Docker 只需要启动 10 个隔离的应用即可。
* 更简单的管理
使用 Docker，只需要小小的修改，就可以替代以往大量的更新工作。所有的修改都以增量的方式被分发和更新，从而实现自动化并且高效的管理。



# Docker通常用于如下场景：

---



- web应用的自动化打包和发布；
- 自动化测试和持续集成、发布；
- 在服务型环境中部署和调整数据库或其他的后台应用；
- 从头编译或者扩展现有的OpenShift或Cloud Foundry平台来搭建自己的PaaS环境。




#  Docekr与传统虚拟化方式(kvm)对比

---
使用kvm(openstack)  docker 的目的都是为了`提高设备利用率 降低使用成本` ，但`不适用高性能计算的场景`。
下面的图片比较了 Docker 和传统虚拟化方式(kvm)的不同之处，可见容器是在操作系统层面上实现虚拟化，直接复用本地主机的操作系统，而传统方式则是在硬件层面实现。

![docker.png][26]
![virtualization.png][30]
>| 类别 | docker | openstack | 
 | :-------------: |:-------------:| -----:| 
 | 部署难度 |  非常简单| 组件多，部署复杂 |
 | 启动速度 | 秒级|分钟级 |
 | 执行性能 | 和物理系统几乎一致| VM会占用一些资源≈6%-8% |
 | 镜像体积 | 镜像是MB级别| 虚拟机镜像GB级别 |
 | 管理效率 | 管理简单| 组件相互依赖，管理复杂 |
 | 隔离性 |  隔离性高 | 彻底隔离 |
 | 可管理性 | 单进程、不建议启动SSH |完整的系统管理 |
 | 网络连接 | 比较弱 | 借助Neutron可以灵活组件各类网络架构 |
# Docker 8个优点

---
![8_docekr_use_cases.png][22]

* Simplifying configuration 简化配置 灵活
* Developer productivity  提高开发效率
* Server consolidation  服务器整合
* Multi tenancy 多租户使用
* Rpaid deployment 快速部署
* Code  Pipeline management 代码流水线管理
* App Isolation 应用的隔离
* Debugging capabilities 代码调试




# Docker引擎

---
docker引擎是一个c/s结构的应用，主要组件见下图：

![engine-components-flow.png][28]

- Server是一个常驻进程
- REST API 实现了client和server间的交互协议
- CLI 实现容器和镜像的管理，为用户提供统一的操作界面








#Docker 架构

---
>Docker使用C/S架构，Client 通过接口与Server进程通信实现容器的构建，运行和发布。client和server可以运行在同一台集群，也可以通过跨主机实现远程通信。



![architecture.jpg][23]


# Docker 组件

---
>- 镜像(image)
Docker 镜像（Image）就是一个只读的模板。例如：一个镜像可以包含一个完整的操作系统环境，里面仅安装了 Apache 或用户需要的其它应用程序。镜像可以用来创建 Docker 容器，一个镜像可以创建很多容器。Docker 提供了一个很简单的机制来创建镜像或者更新现有的镜像，用户甚至可以直接从其他人那里下载一个已经做好的镜像来直接使用。
镜像（Image）就是一堆只读层（read-only layer）的统一视角，也许这个定义有些难以理解，看看下面这张图：

![image_ufs.png][29]
>右边我们看到了多个只读层，它们重叠在一起。除了最下面一层，其它层都会有一个指针指向下一层。这些层是Docker内部的实现细节，并且能够在docker宿主机的文件系统上访问到。统一文件系统（Union File System）技术能够将不同的层整合成一个文件系统，为这些层提供了一个统一的视角，这样就隐藏了多层的存在，在用户的角度看来，只存在一个文件系统。

- 仓库(repository)
仓库（Repository）是集中存放镜像文件的场所。有时候会把仓库和仓库注册服务器（Registry）混为一谈，并不严格区分。实际上，仓库注册服务器上往往存放着多个仓库，每个仓库中又包含了多个镜像，每个镜像有不同的标签（tag）。
仓库分为公开仓库（Public）和私有仓库（Private）两种形式。最大的公开仓库是 Docker Hub，存放了数量庞大的镜像供用户下载。国内的公开仓库包括 时速云 、网易云 等，可以提供大陆用户更稳定快速的访问。当然，用户也可以在本地网络内创建一个私有仓库。
当用户创建了自己的镜像之后就可以使用 push 命令将它上传到公有或者私有仓库，这样下次在另外一台机器上使用这个镜像时候，只需要从仓库上 pull 下来就可以了。
Docker 仓库的概念跟 Git 类似，注册服务器可以理解为 GitHub 这样的托管服务。

- 容器(container)
Docker 利用容器（Container）来运行应用。容器是从镜像创建的运行实例。它可以被启动、开始、停止、删除。每个容器都是相互隔离的、保证安全的平台。可以把容器看做是一个简易版的 Linux 环境（包括root用户权限、进程空间、用户空间和网络空间等）和运行在其中的应用程序。
容器的定义和镜像几乎一模一样，也是一堆层的统一视角，唯一区别在于容器的最上面那一层是可读可写的。
![container-ufs.png][25]
一个运行态容器被定义为一个可读写的统一文件系统加上隔离的进程空间和包含其中的进程。下面这张图片展示了一个运行中的容器。
![container-running.png][24]

正是文件系统隔离技术使得Docker成为了一个非常有潜力的虚拟化技术。一个容器中的进程可能会对文件进行修改、删除、创建，这些改变都将作用于可读写层。

---

#  Docker 安装

自17年开始，docker分为docker-ce（社区版）、docker-ee（企业版），另外docker-io是较早的版本，通常用的都是docker-ce版；
目前CentOS内核对docker支持情况：
a. CentOS7必须是64位、系统内核版本为 3.10 以上。
b. CentOS6.5或更高的版本的CentOS6上，要求系统为64位、系统内核版本为 2.6.32-431 或者更高版本。

## 使用官方安装脚本自动安装：

```sh
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```
	--mirror Aliyun通过国内站阿里云加速
## 手动安装
###Ubuntu 14.04 16.04 (使用apt-get进行安装)
1: 安装必要的一些系统工具
```sh
sudo apt-get update
sudo apt-get -y install apt-transport-https ca-certificates curl software-properties-common
```
2: 安装GPG证书
```sh
curl -fsSL http://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add 
```
3: 写入软件源信息
```sh
sudo add-apt-repository "deb [arch=amd64] http://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
```
4: 更新并安装 Docker-CE
```sh
sudo apt-get -y update
sudo apt-get -y install docker-ce
```
####安装指定版本的Docker-CE:
1: 查找Docker-CE的版本:
```sh
apt-cache madison docker-ce
docker-ce | 17.03.1~ce-0~ubuntu-xenial | http://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial/stable amd64 Packages
docker-ce | 17.03.0~ce-0~ubuntu-xenial | http://mirrors.aliyun.com/docker-ce/linux/ubuntu xenial/stable amd64 Packages
```
 2: 安装指定版本的Docker-CE: (VERSION 例如上面的 17.03.1~ce-0~ubuntu-xenial)
```sh
sudo apt-get -y install docker-ce=[VERSION]
```

---

###CentOS 7 (使用yum进行安装)
1: 安装必要的一些系统工具
```sh
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```
2: 添加软件源信息
```sh
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
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
`注意`：
官方软件源默认启用了最新的软件，您可以通过编辑软件源的方式获取各个版本的软件包。例如官方并没有将测试版本的软件源置为可用，你可以通过以下方式开启。同理可以开启各种测试版本等。
```sh
vim /etc/yum.repos.d/docker-ce.repo
```
将 `[docker-ce-test]` 下方的 `enabled=0` 修改为 `enabled=1`

#### 安装指定版本的Docker-CE:
1: 查找Docker-CE的版本:
```sh
yum list docker-ce.x86_64 --showduplicates | sort -r
```
	 Loading mirror speeds from cached hostfile
	Loaded plugins: branch, fastestmirror, langpacks
	docker-ce.x86_64            17.03.1.ce-1.el7.centos            docker-ce-stable
	docker-ce.x86_64            17.03.1.ce-1.el7.centos            @docker-ce-stable
	docker-ce.x86_64            17.03.0.ce-1.el7.centos            docker-ce-stable
	Available Packages
2 : 安装指定版本的Docker-CE: (VERSION 例如上面的 17.03.0.ce.1-1.el7.centos)
```sh
sudo yum -y install docker-ce-[VERSION]
```

---

#卸载 Docker
卸载Docker安装包：

```sh
sudo yum remove docker-ce
```
删除 镜像 容器  卷 Images, containers, volumes:
```sh
 sudo rm -rf /var/lib/docker
```
必须手动删除任何已编辑的配置文件。

---
# Docker镜像和容器
### Docker搜索centos镜像
```sh
docker search centos
```
	  NAME                               DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
	  centos                             The official build of CentOS.                   4585      [OK]       
	  ansible/centos7-ansible            Ansible on Centos7                              115                  [OK]
	  jdeathe/centos-ssh                 CentOS-6 6.10 x86_64 / CentOS-7 7.5.1804 x...   99                   [OK]
	  consol/centos-xfce-vnc             Centos container with "headless" VNC sessi...   60                   [OK]
	  imagine10255/centos6-lnmp-php56    centos6-lnmp-php56                              44                   [OK]
	  tutum/centos                       Simple CentOS docker image with SSH access      43                   
	  centos/mysql-57-centos7            MySQL 5.7 SQL database server                   38                   
	  gluster/gluster-centos             Official GlusterFS Image [ CentOS-7 +  Glu...   32                   [OK]
	```
	  
 
###  Docker 拉取镜像

```sh
 docker pull centos
```
	latest: Pulling from centos
	675ac122cafb: Pull complete 
	a4875ffe6057: Pull complete 
	c5507be714a7: Pull complete 
	Digest: sha256:5d91c5535c41fd1bb48d40581a2c8b53d38fc2eb26df774556b53c5a0bd4d44e
	Status: Downloaded newer image for centos:latest
 
### Docker 查看镜像image
```bash
docker images
```
	REPOSITORY              TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
	centos                  latest              c5507be714a7        9 days ago          199.7 MB
	jenkins/jenkins         latest              ce76f60a8689        4 weeks ago         700.6 MB
	jenkins/jenkins         lts                 dd6245527881        9 weeks ago         700 MB
### Docker删除镜像
```sh
docker rmi  image id
```
## Docker helloword

```sh
docker run centos /bin/echo  'hello word '
```
	输出：	hello word
各个参数解析：

- **docker**: Docker 的二进制执行文件。
- **run**:与前面的 docker 组合来运行一个容器。
* **centos**：指定要运行的镜像，Docker首先从本地主机上查找镜像是否存在，如果不存在，Docker 就会从镜像仓库 Docker Hub 下载公共镜像。
* **/bin/echo "Hello world"**: 在启动的容器里执行的命令

以上命令完整的意思可以解释为：Docker 以centos 镜像创建一个新容器，然后在容器里执行 bin/echo "Hello world"，然后输出结果。

```sh
docker ps -a 
```
	输出：	CONTAINER ID        IMAGE                       COMMAND                CREATED              STATUS                          PORTS               NAMES
			容器ID             镜像                         命令                  创建时间              启动状态                         端口                  容器名称
		  635e3e5bf369        centos                      "/bin/echo 'hello wo   About a minute ago   Exited (0) About a minute ago                       condescending_curie 
### 运行交互式的容器
通过docker的两个参数 -i -t，让docker运行的容器实现"对话"的能力
```sh
docker run --name mydocker -it centos /bin/bash
```




未完待续

---
版权声明：本博文内容均来自互联网，侵删
参考：[Get Docker CE for CentOS][49]
参考：[海牛部落－青牛][50]http://hainiubl.com/topics/13
参考：[Docker CE 镜像源站][51]https://yq.aliyun.com/articles/110806




[21]: http://img.caojie.top/kspn/images/docker/576507-docker1.png
[22]: http://img.caojie.top/kspn/images/docker/8_docekr_use_cases.png
[23]: http://img.caojie.top/kspn/images/docker/architecture.jpg
[24]: http://img.caojie.top/kspn/images/docker/container-running.png
[25]: http://img.caojie.top/kspn/images/docker/container-ufs.png
[26]: http://img.caojie.top/kspn/images/docker/docker.png
[27]: http://img.caojie.top/kspn/images/docker/docker_logo.png
[28]: http://img.caojie.top/kspn/images/docker/engine-components-flow.png
[29]: http://img.caojie.top/kspn/images/docker/image_ufs.png
[30]: http://img.caojie.top/kspn/images/docker/virtualization.png















[49]: https://docs.docker.com/install/linux/docker-ce/centos/
[50]: http://hainiubl.com/topics/13
[51]: https://yq.aliyun.com/articles/110806
