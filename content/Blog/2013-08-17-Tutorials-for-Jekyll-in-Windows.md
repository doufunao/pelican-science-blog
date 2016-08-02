---
layout: post
title: 如何在Windows 7下进行Jekyll本地调试
tags: ['Jekyll']
categories: ['Tutorials']
published: true
date: 2013-08-21 2:12pm
---
####目录
-   [0 罗罗嗦嗦](#background)
-	[1 准备](#preparation)
-	[2 安装Ruby以及Jekyll](#installation)
-	[3 初始化一个网站](#initialization)
-	[4 本地运行](#running)
-	[5 参考文档](#documents)


####0 罗罗嗦嗦 { #background }
>本文适合Ruby小白，第一次用Jekyll建站，能看Html+CSS的孩纸。

####1 准备 { #preparation}
-	Windows 7 32位 *后面下载的两个软件要注意版本，本文给出的链接都是32位的软件*
-	RubyInstaller [Ruby 2.0.0-p247](http://dl.bintray.com/oneclick/rubyinstaller/rubyinstaller-2.0.0-p247.exe?direct)
-	Development Kit [DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe](http://rubyforge.org/frs/download.php/76805/DevKit-mingw64-32-4.7.2-20130224-1151-sfx.exe)

以上两个程序可以到[官网](http://www.rubyinstaller.org/downloads/)下载最新版本

<!--break-->

####2 安装Ruby以及Jekyll { #installation }

#####第一步 安装Ruby
-	运行Ruby 2.0.0-p247.exe，默认路径是C:\Ruby200本文以此为例
-	运行DevKit-tdm-32-4.5.2-20111229-1559-sfx.exe解压到任意文件夹下，本文以C:\DevKit为例
-	打开cmd，cd到C:\DevKit,输入

	`ruby dk.rb init`

	`ruby dk.rb install`

	*如果第二步的命令都能成功运行，说明安装成功了。*
	*如果不成功，可以试一下[RailsInstaller](http://railsinstaller.org/en)，直接运行，无需安装前面两个文件。	
	*由于我最先看的文档是Jekyll官方给的参考博客，没有试过这个，目测比我这么折腾方便orz...

#####第二步 安装Jekyll
-	打开命令行(cmd)，输入  
	`gem sources --remove http://rubygems.org/`     
    `gem sources -a http://ruby.taobao.org/`   
	上面这个代码的作用是添加国内镜像
-	运行上面的代码提示成功后，继续输入  
	`gem install jekyll`	
	>基本上上面的步骤完成后就没啥问题了。不放心再安装个rdiscount  
	>`gem install rdiscount`

*解决中文编码问题*    
打开C:\Ruby200\lib\ruby\gems\2.0.0\gems\jekyll-1.1.2\lib\jekyll\convertible.rb,找到第31行，把
	`self.content = File.read(File.join(base, name))`

修改为  
	`self.content = File.read(File.join(base, name), :encoding => "utf-8")`

(到了这里，就算Jekyll安装完成了。)

####3 初始化一个网站{ #initialization }
-	在你中意的硬盘下建立一个空文件夹，这个空文件夹以后就是网站的根目录。本文以D:\MyBlog为例
-	在D:\MyBlog下分别建立`_posts`,`_layouts`两个文件夹，以及`_config.yml`文件，*yml是文件后缀名。以后要发布的博客文章就放在`_posts`文件夹里，`_layouts`用来放模板文件*

目录树

<pre><code>D:/MyBlog/ 
|-- _layouts  
|-- _posts
|-- _config.yml</code></pre>

####4 本地运行{ #running }
用记事本新建一个文件，输入`"Hello,MyBlog"`，保存在D:\MyBlog下，文件名命名为index.html，*注意保存的时候文件类型选择`"全部文件"`*.
打开命令行(cmd)，cd至D:\MyBlog目录，在当前目录下输入

`jekyll serve`

或者

`jekyll serve -w`

参数`"-w"`的意思是即使检测文件的更新，即watch之意。若你在本地浏览网站的时同时修改本地文件，加入此参数Jekyll服务器便会检测到，这样你便能及时浏览修改后的网页等。*`_config.yml`修改后需重新启动Jekyll服务器*

在浏览器中输入

`http://localhost:4000`

便可以看到你的Hello,MyBlog了~

####5 参考文档{ #documents }

1.[Jekyllrb.com][1]：应该是官方文档吧，看的最多，关于配置和参数的一些问题都可以在这里找到答案。
2.[Github Pages极简教程][2]：简单易懂，解释很清楚，与网站相关的模块也有说。
3.[How to install JekyII under windows][3]：清晰
4.[Markdown语法说明][4]：学习Markdown语法必看，不解释。
5.[搭建一个免费的，无限流量的Blog----github Pages和Jekyll入门][5]：图文并茂。作者的示例是在项目里建网站，项目的wiki page？

在安装的过程中，发现了N多问题，有些已解决有些未解决，总的来说还算顺利。貌似Jekyll是在近两年兴起，常见问题都可以百度谷歌解决，遇到问题再说吧。

[1]:http://jekyllrb.com/
[2]:http://yanping.me/cn/blog/2012/03/18/github-pages-step-by-step/
[3]:http://markdingst.blogspot.com/2013/06/how-to-install-jekyii-under.html
[4]:http://wowubuntu.com/markdown/
[5]:http://www.ruanyifeng.com/blog/2012/08/blogging_with_jekyll.html