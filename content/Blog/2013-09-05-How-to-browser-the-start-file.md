---
layout: post
title: Axure生成的Html原型页面浏览方法及其原因解释
tags: ['prototype design','Axure RP']
categories: ['method','guide']
published: true
date: 2013-09-07 00:07 AM
---

##目录
-  0	[原型页面所在文件夹的结构示意图](#c0)
-  1	[无导航浏览原型文件](#c1)
-  2	[有导航浏览原型文件(推荐)](#c2)
-  3	[关于使用360浏览器、搜狗浏览器等浏览器浏览时不能访问start.html或index.html的问题](#c3)

<!--break-->

##0	原型页面所在文件夹的结构示意图 { #c0 }
![How-to-browser-the-start-file](/assets/2013-09-06_235128.png)
##1	无导航浏览原型文件 { #c1 }
直接双击任意html文件或使用浏览器打开html文件即可查看其内容.
##2	有导航浏览原型文件(推荐) { #c2 }
###2.1找到start.html文件
![How-to-browser-the-start-file](/assets/2013-09-07_000431.png)
###2.2点击右键-打开方式-Internet Explorer
![How-to-browser-the-start-file](/assets/2013-09-06_235258.png)
###2.3在打开的IE浏览器窗口中会出现控件安装的提示，允许阻止的内容即可，如下图所示
![How-to-browser-the-start-file](/assets/2013-09-06_235344.png)

![How-to-browser-the-start-file](/assets/2013-09-06_235418.png)

###2.4含导航的页面
![How-to-browser-the-start-file](/assets/2013-09-06_235611.png)
##3	关于使用360浏览器、搜狗浏览器等浏览器浏览时不能访问START.HTML或INDEX.HTML的问题 { #c3 }
*问题：*

如果使用搜狗浏览器或者360浏览器直接打开start.html或index.html文件（直接打开其他页面并不会出现这个问题），会跳转到一个提示页面。页面上会显示Install the Axure RP Extension For Chrome ，意思是为Chrome安装一个Axure RP的扩展。
![How-to-browser-the-start-file](/assets/2013-09-07_000233.png)

这个问题目前没有好的解决办法，所以不管是在搜狗浏览器还是在360浏览器都无法正常浏览Axure RP生成的导航页面（start.html或index.html）。

*原因：*

国内主流浏览器基本上都采用chrome的内核，所以Axure在识别浏览器的时候将国内的浏览器都识别为chrome浏览器。Axure在chrome浏览start.html时需要安装一个扩展插件，但是这个插件只能在chrome的应用商店里下载到（Axure提示页面里的下载链接也是指向chrome的应用商店），国内的浏览器是无法安装的。所以这条路不通。

再说chrome浏览器。chrome的应用商店是墙外的世界，不翻墙的普通用户是无法下载到的，所以这条路也堵死了。

*解决办法：*
-  0 会翻墙的朋友可以直接按照提示在chrome安装扩展。
-  1 普通用户推荐使用IE直接浏览。
-  2 另外经测试，Firefox也可以直接浏览，推荐使用。Opera未测试。