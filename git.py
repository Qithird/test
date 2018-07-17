
gittutorial-Git的教程介绍
Git是一个快速，可扩展的分布式版本控制系统，具有异常丰富的命令集，可提供高级操作和对内部的完全访问

1.git项目管理

#获取命令文档帮助
man git-log  或者  git help log
#配置个人信息
git config --global user.name 'py.qi'
git config --global user.email 'qi@163.com'

#导入新项目：
tar xf project.tar.gz
cd project
git init
#或者在空文件目录
git init
#它会初始化工作目录，并创建一个名为".git"的新目录

#提交到仓库
git add test.py #将文件提交到索引index
    -n #只显示文件不添加文件
    -v #显示详细
    -f #强制添加被忽略的文件
    -i #在树结构中添加修改文件内容
#add只是把文件添加到临时暂存区域中了，使用commit将索引中的内容永久存储在存储库中：
git commit -m 'add test' #提交到仓库


#查看工作区状态
git status
#查看修改的内容
git diff test.py
git diff HEAD -- test.py
git diff --cached  #显示进行的更改但未添加到索引中的内容

#查看提交历史
git log
git log --pretty=oneline #简短输出信息
git log --graph --pretty=oneline --abbrev-commit 

#退回到上一个版本
git reset --hard HEAD^

#前进到下一个版本
git reflog #查看历史命令，找到commit_id
git reset --hard 3b13954 #通过ID前进到下一个版本

#撤销修改
#当文件只是在工作区修改了,要撤销修改使用以下命令
git checkout -- test.py
#当文件修改提交到缓存区后，想要撤销修改需要先从缓存区丢弃修改然后再在工作区撤销即可
git reset HEAD test.py
git checkout -- test.py
#当文件修改被提交到版本库后，想要撤销修改就需要使用版本回退了
git reset --hard HEAD^


#删除文件
#如果文件被删除了需要在版本中将文件删除
rm test.txt
git rm test.txt
git commit -m 'remove test.txt'
#如果文件是被误删的，可以使用以下命令恢复或者退回到上一个版本
git checkout -- text.txt #如果文件还在版本库中使用此命令
git reset --hard HEAD^ #如果文件被彻底删除了可以回退到上要给版本

2.远程仓库
#要添加到远程仓库首先需要注册一个github账号
#在本地创建SSH key执行以下命令，一路回车即可，它会在用户目录下生成一个.ssh文件夹，里面创建了两个文件id_rsa为私钥文件自己使用的，一个是id_rsa.pub为公钥文件，需要上传到github网站上
ssh-keygen.exe -t rsa -C "920664709@163.com"
#登陆github账号，选择设置，在设置中找到SSH keys然后点击add SSH Key添加公钥，随便写个标题，将我们创建的公钥内容粘贴进来，保存即可
#关联远程库
#在命令行创建新的存储库
echo "#spider-test" >> README.md
git init
git add README.md
git commit -m "first commit"
#关联远程存储库
git remote add origin git@github.com:Qithird/Spider-12306.git
#查看远程仓库的名字,-v显示详细
git remote -v
#5.推送分支的所有内容
git push -u origin master
#推送更新
git push origin master
#删除远程库关联
git remote rm origin
#显示远程关联仓库
git remore -v
#显示关联库的详细信息
git remote show gitee
#添加一个远程库
git remote add test url
#从远程仓库下载所有更改，但不更新到HEAD
git fetch github
#从远程仓库下载所有更改并合并到HEAD中
git pull github master
#删除远程分支
git branch -dr github/matser
#克隆远程仓库
git clone git@github.com:Qithird/Spider-12306.git

#使用GitHub和码云
#如在GitHub上想参与某个项目，可以直接在项目的主页点击fork功能将项目克隆到自己的仓库中，然后通过命令克隆到本地进行修改和提交

#使用码云：https://gitee.com/
#关联码云：
git remote add gitee git@gitee.com:Qithird/test.git
#同时关联github
git remote add github git@github.com:Qithird/test.git
#查看关联
git remote -v
gitee	git@gitee.com:Qithird/test.git (fetch)
gitee	git@gitee.com:Qithird/test.git (push)
github	git@github.com:Qithird/test.git (fetch)
github	git@github.com:Qithird/test.git (push)

#推送到github和码云
git push github master
git push gitee master

#拉取远程仓库更新
git pull github master 
git pull gitee master 

3.分支管理
#每次提交git会将修改提交到master分支上，HEAD指针指向master，而当我们创建新分支后HEAD则指向新分支，表示当前分支
#查看分支
git branch
#创建分支
git branch <name>
#切换分支
git checkout <name>
#创建+切换分支
git checkout -b <name>
#合并某分支到当前分支
git merge <name>
#删除分支
git branch -d <name>
#查看分支合并图
git log --graph
#删除一个没有被合并过的分支使用-D强行删除
git branch -D <name>

#开发中不要在master分支上开发，而是在dev分支上，在合并分支是加上--no-ff参数可以用普通模式合并，合并后历史记录有分支信息

#暂时存储分支，如在工作中接到临时任务需要处理，而当前的分支任务没完成无法提交时，可以使用stash功能来将当前工作现场储藏起来，等完成后再恢复现在即可
git stash #储藏现场分支
git stash list #查看stash
git stash pop #恢复现场并删除stash
git stash apply #只恢复现在不删除stash,继续可以上面的命令删除stash

#删除一个没有被合并过的分支使用-D强行删除
git branch -D <name>

#推送分支
git push origin branch-name
#抓取远程的新提交
git pull
#建立本地分支与远程分支的关联
git branch --set-upstream branch-name origin/branch-name
#把分叉的提交历史整理成一条直线
git rebase





4.标签管理
git的标签为版本库的快照，它指向某个commit的指针
#打标签，首先需要切换到需要打标签的分子上，然后再执行打标签
git checkout master
git tag v1.0
git tag  #查看所有标签

#默认标签是打在最新的commit上的，如果需要打在之前的commit上就需要查找到commit的id然后通过id给commit打上标签
git log --pretty=oneline --abbrev-commit #查看历史commit
git tag v0.9 commit_id

#查看标签信息
git show v0.9
#使用-a指定标签名，-m指定说明，来创建带说明的标签
git tag -a v1.1 -m 'version 1.1 rebase' commit_id

#删除标签
git tag -d v0.1
#推送标签到远程库
git push origin v1.0
git push origin --tags  #推送所有标签
#删除远程标签
git push origin :refs/tags/<tagname>




5.自定义git
#我们已经通过user.name和user.email来配置了用户的个人信息了
#我们还可以配置更多选项如，让git显示颜色
git config --global color.ui true


#忽略特殊文件
#在项目中新建.gitignore文件写入要忽略文件的后缀，可以从以下网站找到配置好的忽略文件:https://github.com/github/gitignore

#然后将忽略的文件.gitignore提交到远程代码库中
git add .gitignore
git commit -i 'add gitignore'
git push github master

#如果要添加的文件被gitignore忽略了，可以使用-f强制添加
git add -f app.class
git commit -i 'add -f aap-class'
git push github master

#如果是.gitignore文件有问题可以通过命令检查看是哪条命令忽略了文件
git check-ignore -v app.class


6.配置别名
#如将提交到远程仓库的命令设置别名为pg
git config --global alias.pg 'push github master'

#配置历史纪录查看别名
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

#配置git的时候加上--global是针对当前用户起作用，如果不加则对当前的仓库起作用，每个仓库的配置文件放在.git/config中，别名在[alias]后面，要删除别名可以直接删除对应的行即可，对于当前用户的git配置文件放在用户主目录下的一个隐藏文件.gitconfig中，配置别名也可以直接修改这个文件:

# cat gitee/.git/config 
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[branch "master"]
[remote "gitee"]
	url = git@gitee.com:Qithird/test.git
	fetch = +refs/heads/*:refs/remotes/gitee/*
[remote "github"]
	url = git@github.com:Qithird/test.git
	fetch = +refs/heads/*:refs/remotes/github/*
[branch "master"]
	remote = gitee
	merge = refs/heads/master



#cat .gitconfig
[user]
        name = Qithird
        email = 920664709@163.com
[color]
        ui = true
[alias]
        lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit




7.搭建git服务器
(1)安装git
yum install git 
(2)创建git用户
useradd git
(3)创建证书登陆
手机所有需要登陆的用户的公钥，将所有公钥导入到/home/git/.ssh/authorized_keys文件中。一行一个
(4)初始化Git仓库
#首先创建一个目录作为仓库
mkdir sample.git
#然后初始化仓库
git init --bare sample.git
#修改仓库的属组
chown -R git.git sample.git
(5)禁用shell登陆
git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell
(6)克隆远程仓库
git clone git@ip:/sample.git





#windows系统下命令行报错：
warning: LF will be replaced by CRLF in readme.txt.
The file will have its original line endings in your working directory.
#解决方法：
rm -rf .git
git config --global core.autocrlf false
