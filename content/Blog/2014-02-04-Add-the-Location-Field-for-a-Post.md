---
title: Jekyll文章自动显示写作地点
date: 2014-02-04 11:22AM
layout: post
location: 武威老家
tags: ['jekyll','blog','yaml']
categories: ['Tutorials','Notes']
---
突然想着能不能自动加个字段显示地点，然后就随便试了一下，竟然成功了。

- [启发]( #start )
- [添加location字段]( #trial-step01 )
- [在文章中显示location]( #trial-step02 )
##启发 { #start }

在写博客的时候可以预先定义几个字段，比如title，date，layout等

	title: Jekyll为文章增加地点字段
	date: 2014-02-04 11:22AM
	layout: post

我就想着，那我再增加一个地点呗。
走起~

<!--break-->
##添加locatioin字段 { #trial-step01 }

首先，在yaml的定义里直接加上location:loc
<pre><code>---<br>title: test <br>date: 2014-02-04 <br>location: loc <br>---</code></pre>

>PS. 输入三个&minus;可真是费劲...最后还是用直接写html来实现的：
>
>``<pre><code>---<br>title: test<br>date: 2014-02-04<br>location: loc<br>---</code></pre>``

然后，在正文部分写上
	
	{{ page.location }}

运行着

	>jekyll serve -w

看看效果，成功！

![成功显示location字段](\assets\2014-02-04_01.png)

------------------
##在文章中显示location { #trial-step02 }

继续折腾。在博客的最后我想加上“于XXX地点”几个字，“于”肯定是不变的，“XXX地点”毫无疑问就是``page.location``变量。新问题出现了，万一我在写页头的时候没有加上location肿么办？埋头。

仿着分页的代码，我写下了如下语句：

	{% if page.location == "" %}
	地点为空
	{% else %}
	地点不为空
	{% endif %}

一测试，至少没有问题。

![成功执行语句](\assets\2014-02-04_02.png)

本着要不不整，整就整到底的精神，继续测试。把location这个字段直接从页头里去掉，然后再生成一遍博客。

![地点为空的判断句没有执行](\assets\2014-02-04_03.png)

发现地点为空的判断句没有执行。于是乎继续翻到分页的代码，发现判断是否有前一页的语句并没有加上等号。于是乎，模仿之，我也不加。将代码改为

	{% if page.location %}
	地点不为空
	{% else %}
	地点为空
	{% endif %}

>这里我直接理解location如果存在就为true，不存在就为false

再测试，好像没有什么问题。

![好像没有什么问题](\assets\2014-02-04_04.png)

>注意，此时是没有location字段的，前面已经删掉了。

再把location加上试试。

1.	location有值的情况：`location: loc`

![location有值](\assets\2014-02-04_05.png)

2.	location无值的情况：`location: `

![location无值](\assets\2014-02-04_06.png)

成功！

到此为止，经过各种试验，完整代码如下：

	>在模板页希望显示写作地点的地方加入
		    {% if page.location %}
            <span class="location">于{{ page.location }}</span></br>
            {% else %}
            <span class="location">于幻想乡</span></br>
            {% endif %}

    >在md页面的页头加入
    		location: loc

即可实现在博文页面自动显示写作地点（loc）的功能。

这样每次只要在页头的定义手动加入`location`字段，该字段即可自动显示在文章中。