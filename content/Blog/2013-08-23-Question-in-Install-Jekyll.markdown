---
layout: post
title: 在本地安装Jekyll时遇到的几点问题
date: 2013-08-23 05:27pm
published: true
categories: ['question','Jekyll']
tags: ['Jekyll','paginator','jekyllrb.com']
---
遇到的问题做个记录~
##1.每修改一次_config.yml文件都要重新运行jekyll serve一次

为了实现分页的功能，需要在_config.yml里设置paginate的值，比如

	paginate: 10
	
表示每页显示十个post

##2.paginator这个参数只能在index.html里调用

还是为了实现分页功能，整了半天才发现这个问题，其实在jekyllrb.com里已有提示(Tips)。

<!--break-->

##3.如何解决首行空两个格的问题

解决办法：修改CSS，找到P的CSS属性定义，加入`text-indent: 2em;`就ok了。例如：

	.post p{
		text-indent: 2em;
		}

##4.首页显示摘要的问题

1)paginator变量只能用在index.html的页面中

在Jekyll中生成post列表，主要用的是paginator变量，但是并不是所有页面都可以使用，只有在index.html的页面中才能调用这个变量。当时查了好久，最后发现其实jekyllrb.com上早有提示。生成列表的代码：

	{% for post in paginator.posts %}
		{{ post.title }}       <!--输出博文的标题-->
		{{ post.content }}     <!--输出博文的正文-->
		{{ post.date }}        <!--输出博文的日期-->
	{% endfor %}


2)利用liquid的过滤器和注释标签实现段落摘要

纯手工操作\\(^o^)/~

选取每页的前几段为摘要（你也可以选择指定的段落，不过在首页输出的时候就相对麻烦一些，但是基本方法相似），至于是哪几段自己决定。例，有段落一、段落二、段落三，把段落一作为摘要，其代码如下所示：

	<p>段落一</p>
	<!--break-->
	<p>段落二</p>
	<p>段落三</p>

**也就是编辑博文时在文中的`段落一`与`段落二`之间加入`<!--break-->`。**如果是在markdown文件中，就变成：

	段落一
	
	<!--break-->

	段落二

	段落三

接下来开始编辑首页文件。插入文章列表的方法不说了，直接上代码。原来的代码是

	{% for post in paginator.posts %}
		{{ post.content }}
	{% endfor %}

修改为

	{% for post in paginator.posts %}
		{{ post.content | split:'<!--break-->' | first }}
	{% endfor %}

**也就是在"博文变量.content"后面加上 `| split:'<!--break-->' | first `**

ok，简易摘要完成。

---

其他问题

markdown的编译程序(processor)对于一些语句会报错，最后导致页面无法生成。其实现在还有点迷糊，难道markdown没有统一吗？在学markdown的时候用一些语句做测试，就会出现报错。