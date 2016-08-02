---
title: Windows上安装easy_install
layout: post
published: true
date: 2014-02-01 22:46
tags: ['python', 'easy_install', 'setuptool']
categories: ['Tutorials', 'Notes']
location: 武威老家
---

第一步，在官网下载[ez_setup.py](https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py)文件[https://pypi.python.org/pypi/setuptools#downloads](https://pypi.python.org/pypi/setuptools#downloads)，在命令行cmd里编译执行ez_setup.py

	>python ez_setup.py

<!--break-->

第二步，在环境变量path里增加个路径

	C:\python33\scripts

第三步，利用easy_install安装BeautifulSoup4。在命令行cmd里输入

	>easy_install beautifulsoup4

参考链接：

1. [python-easy_install的安装和使用](http://www.cnblogs.com/huangjacky/archive/2012/03/28/2421866.html)
2. [setuptool官网](https://pypi.python.org/pypi/setuptools#downloads)
