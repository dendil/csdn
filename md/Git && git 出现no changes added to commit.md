今天发现了一个问题
在git 目录修改文件后发现 无法 commit 
```bash
xxxx@xxxxx MINGW64 /d/xxx/xxxx (master)
$ git commit
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
        modified:   README.md
        modified:   java.lang.md

no changes added to commit
```


解决方法是：

1. 
```bash
 git add  .     <-----------注意 “.”
```
2
```bash
git  status
```
3
```bash
git commit -m  "description" 
```











.
