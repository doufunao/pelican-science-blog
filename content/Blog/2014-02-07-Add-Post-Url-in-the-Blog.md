---
title: Jekyll添加内部链接
date: 2014-02-07 19:23
layout: post
location: 家
tags: ['']
categories: ['']
---
问题：在文章中直接添加另一篇文章的链接

描述：

由于在markdown里加入链接的时候，由于文章链接是由jekyll生成的，所以无法获知post的相对路径。(虽然根据规则可以推断出，但是万一以后规则改变或者某些变量被修改了，原先写好的路径就会失效)

<!--break-->

在网上搜了一下，解决办法还是很简单的，在需要插入链接的地方写上。

<pre><code>&#123;% post_url 2014-02-04-Add-the-Location-Field-for-a-Post %&#125;</code></pre>


格式：

	post_url 文件名

>注意：大小写

PS.`{`和`%`没有办法连在一起显示，最后还是直接写html实现的。

	<pre><code>&#123;% post_url 2014-02-04-Add-the-Location-Field-for-a-Post %&#125;</code></pre>

其中，`&#123;`和`&#125;`分别表示`{`和`}`

来源：[github page (Jekyll) 的一些问题](http://www.v2ex.com/t/93507)